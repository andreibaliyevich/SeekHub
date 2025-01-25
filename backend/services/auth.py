from pydantic import EmailStr
from exceptions.auth import InvalidCredentialsError
from exceptions.form import InvalidFormDataError
from models.users import Users
from schemas.auth import (
    UserToken,
    RegisterUser,
    PasswordChange,
    UserProfileUpdate,
)
from schemas.profiles import ProfileDetails
from utilities.auth import (
    verify_password,
    get_password_hash,
    create_access_token,
)
from utilities.unit_of_work import AbstractUnitOfWork


class AuthService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def authenticate_user(self, email: EmailStr, password: str):
        user = await self.uow.users_repository.obj_by_email(email)
        if user is None:
            raise InvalidCredentialsError
        if not user.is_active:
            raise InvalidCredentialsError
        if not verify_password(password, user.hashed_password):
            raise InvalidCredentialsError
        access_token = create_access_token(data={"sub": user.email})
        return UserToken(
            access_token=access_token,
            token_type="Bearer",
            name=user.name,
        )

    async def register_user(self, data: RegisterUser):
        user_dict = data.model_dump()
        user_dict["hashed_password"] = get_password_hash(data.password)
        del user_dict["password"]
        del user_dict["confirm_password"]
        new_user = await self.uow.users_repository.add(user_dict)
        await self.uow.session.flush()
        await self.uow.profiles_repository.add({"id": new_user.id})
        await self.uow.commit()
        await self.uow.session.refresh(new_user)
        return new_user

    async def change_password(self, user: Users, data: PasswordChange):
        if not verify_password(data.current_password, user.hashed_password):
            raise InvalidFormDataError({"current_password": "Invalid current password."})
        hashed_password = get_password_hash(data.new_password)
        await self.uow.users_repository.update(user.id, {"hashed_password": hashed_password})
        await self.uow.commit()

    async def get_user_profile(self, user: Users):
        return await self.uow.users_repository.get_full_profile(user.id)

    async def update_user_profile(
        self,
        user: Users,
        body_data: UserProfileUpdate,
    ):
        user_dict = body_data.model_dump(exclude_none=True)
        profile_dict = user_dict.pop("profile", {})
        user = await self.uow.users_repository.update(user.id, user_dict)
        profile = await self.uow.profiles_repository.update(user.id, profile_dict)
        await self.uow.commit()
        await self.uow.session.refresh(user)
        await self.uow.session.refresh(profile)
        user.profile = profile
        return user

    async def delete_user_profile(self, user: Users):
        user_id = await self.uow.users_repository.delete(user.id)
        await self.uow.commit()
        return user_id
