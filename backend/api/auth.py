from typing import Annotated
from fastapi import APIRouter, Form, status
from api.dependencies import LoginFormDep, UserDep, UOWDep
from schemas.auth import (
    UserToken,
    RegisterUser,
    RegisteredUser,
    PasswordChange,
)
from services.auth import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login", response_model=UserToken)
async def login(form_data: LoginFormDep, uow: UOWDep) -> UserToken:
    service = AuthService(uow)
    return await service.authenticate_user(form_data.username, form_data.password)


@router.post(
        "/register",
        response_model=RegisteredUser,
        status_code=status.HTTP_201_CREATED,
)
async def register(
    form_data: Annotated[RegisterUser, Form()],
    uow: UOWDep,
) -> RegisteredUser:
    service = AuthService(uow)
    return await service.register_user(form_data)


@router.post("/password-change", status_code=status.HTTP_204_NO_CONTENT)
async def password_change(
    form_data: Annotated[PasswordChange, Form()],
    user: UserDep,
    uow: UOWDep,
):
    service = AuthService(uow)
    return await service.change_password(user, form_data)


@router.get("/profile")
async def read_users_me(user: UserDep, uow: UOWDep):
    queryset = await uow.user_repository.queryset({})
    return {"user": user, "queryset": queryset}
