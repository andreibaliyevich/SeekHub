from pydantic import EmailStr
from exceptions.auth import InvalidCredentialsError, InvalidFormDataError
from schemas.auth import UserToken, RegisterUser
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
        if data.password != data.confirm_password:
            raise InvalidFormDataError({"password": "The provided passwords do not match."})
        user_dict = data.model_dump()
        user_dict["hashed_password"] = get_password_hash(data.password)
        del user_dict["password"]
        del user_dict["confirm_password"]
        new_user = await self.uow.user_repository.add(user_dict)
        await self.uow.commit()
        await self.uow.session.refresh(new_user)
        return new_user
