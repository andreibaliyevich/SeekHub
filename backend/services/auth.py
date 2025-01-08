from uuid import UUID
from pydantic import EmailStr
from exceptions.auth import InvalidCredentialsError
from exceptions.form import InvalidFormDataError
from models.users import Users
from schemas.auth import UserToken, RegisterUser, PasswordChange
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
        user = await self.uow.user_repository.obj_by_email(email)
        if user is None:
            raise InvalidCredentialsError
        if user.disabled:
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
        new_user = await self.uow.user_repository.add(user_dict)
        await self.uow.commit()
        await self.uow.session.refresh(new_user)
        return new_user

    async def change_password(self, user: Users, data: PasswordChange):
        if not verify_password(data.current_password, user.hashed_password):
            raise InvalidFormDataError({"current_password": "Invalid current password"})
        hashed_password = get_password_hash(data.new_password)
        await self.uow.user_repository.update(user.id, {"hashed_password": hashed_password})
        await self.uow.commit()
