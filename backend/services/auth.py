from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from exceptions.auth import InvalidCredentialsError
from exceptions.data import InvalidDataError
from models.users import Users
from schemas.auth import (
    Token,
    RefreshToken,
    TokenData,
    RegisterUser,
    UserProfileUpdate,
    PasswordChange,
)
from utilities.auth import (
    verify_password,
    get_password_hash,
    create_tokens,
    decode_token,
)
from utilities.logging_utils import logger
from utilities.unit_of_work import AbstractUnitOfWork


class AuthService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def authenticate_user(self, email: EmailStr, password: str):
        user = await self.uow.users_repository.user_by_email(email)
        if user is None:
            raise InvalidCredentialsError("Invalid username or password.")
        if not user.is_active:
            raise InvalidCredentialsError("Invalid username or password.")
        if not verify_password(password, user.hashed_password):
            raise InvalidCredentialsError("Invalid username or password.")
        access_token, refresh_token = await create_tokens(data={"sub": str(user.id)})
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
        )

    async def refresh_tokens(self, data: RefreshToken):
        user_id = await decode_token(token=data.refresh_token, refresh=True)
        if user_id is None:
            raise InvalidCredentialsError()
        token_data = TokenData(id=user_id)
        user = await self.uow.users_repository.obj_by_id(id=token_data.id)
        if user is None:
            raise InvalidCredentialsError()
        if not user.is_active:
            raise InvalidCredentialsError()
        access_token, refresh_token = await create_tokens(data={"sub": str(user.id)})
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
        )

    async def register_user(self, data: RegisterUser):
        user_dict = data.model_dump()
        user_dict["hashed_password"] = get_password_hash(data.password)
        del user_dict["password"]
        del user_dict["confirm_password"]
        try:
            async with self.uow.session.begin():
                new_user = await self.uow.users_repository.add(user_dict)
                await self.uow.session.flush()
                await self.uow.profiles_repository.add({"id": new_user.id})
                await self.uow.session.refresh(new_user)
        except Exception as e:
            await self.uow.rollback()
            logger.error(f"Failed to register user and profile: {e}")
            raise IntegrityError(statement=e.statement, params=e.params, orig=e.orig)
        logger.info(f"User with email {user_dict['email']} registered.")
        return new_user

    async def get_user_with_primary_photo(self, user: Users):
        return await self.uow.users_repository.user_with_primary_photo(user.id)

    async def get_user_profile(self, user: Users):
        return await self.uow.users_repository.user_profile(user.id)

    async def update_user_profile(self, user: Users, data: UserProfileUpdate):
        user_dict = data.model_dump(exclude_none=True)
        profile_dict = user_dict.pop("profile", {})

        updated_user = None
        updated_profile = None

        if user_dict:
            try:
                async with self.uow.session.begin_nested():
                    updated_user = await self.uow.users_repository.update(user.id, user_dict)
                    await self.uow.session.flush()
            except Exception as e:
                logger.error(f"Error updating user: {e}")

        if profile_dict:
            try:
                async with self.uow.session.begin_nested():
                    updated_profile = await self.uow.profiles_repository.update(user.id, profile_dict)
                    await self.uow.session.flush()
            except Exception as e:
                logger.error(f"Error updating profile: {e}")

        if updated_user or updated_profile:
            await self.uow.commit()

        if updated_user:
            await self.uow.session.refresh(updated_user)
        else:
            updated_user = user

        if updated_profile:
            await self.uow.session.refresh(updated_profile)

        updated_user.profile = updated_profile
        return updated_user

    async def change_password(self, user: Users, data: PasswordChange):
        if not verify_password(data.current_password, user.hashed_password):
            raise InvalidDataError({"current_password": "Invalid current password."})
        hashed_password = get_password_hash(data.new_password)
        await self.uow.users_repository.update(user.id, {"hashed_password": hashed_password})
        await self.uow.commit()

    async def delete_user(self, user: Users):
        user_id = await self.uow.users_repository.delete(user.id)
        await self.uow.commit()
        logger.info(f"User with email {user.email} deleted.")
        return user_id
