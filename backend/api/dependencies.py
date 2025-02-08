from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from exceptions.auth import InvalidCredentialsError
from models.users import Users
from schemas.auth import TokenData
from utilities.auth import decode_token
from utilities.unit_of_work import AbstractUnitOfWork, UnitOfWork


async def get_uow():
    async with UnitOfWork() as uow:
        yield uow


UOWDep = Annotated[AbstractUnitOfWork, Depends(get_uow)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_user(token: Annotated[str, Depends(oauth2_scheme)], uow: UOWDep):
    user_id = await decode_token(token=token)
    if user_id is None:
        raise InvalidCredentialsError()
    token_data = TokenData(id=user_id)
    user = await uow.users_repository.obj_by_id(id=token_data.id)
    if user is None:
        raise InvalidCredentialsError()
    if not user.is_active:
        raise InvalidCredentialsError()
    return user


LoginFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]
UserDep = Annotated[Users, Depends(get_user)]
