from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from config import settings
from exceptions.auth import InvalidCredentialsError
from models.users import Users
from schemas.auth import TokenData
from utilities.unit_of_work import AbstractUnitOfWork, UnitOfWork


async def get_uow():
    async with UnitOfWork() as uow:
        yield uow


UOWDep = Annotated[AbstractUnitOfWork, Depends(get_uow)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_user(token: Annotated[str, Depends(oauth2_scheme)], uow: UOWDep):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise InvalidCredentialsError("Could not validate credentials")
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise InvalidCredentialsError("Could not validate credentials")
    user = await uow.users_repository.user_by_email(email=token_data.email)
    if user is None:
        raise InvalidCredentialsError("Could not validate credentials")
    if not user.is_active:
        raise InvalidCredentialsError("Could not validate credentials")
    return user


LoginFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]
UserDep = Annotated[Users, Depends(get_user)]
