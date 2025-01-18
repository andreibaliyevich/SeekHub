from typing import Annotated
from fastapi import APIRouter, Body, Form, status
from api.dependencies import LoginFormDep, UserDep, UOWDep
from schemas.auth import (
    UserToken,
    RegisterUser,
    RegisteredUser,
    PasswordChange,
    UserProfile,
    UserProfileUpdate,
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


@router.get("/profile", response_model=UserProfile)
async def profile(user: UserDep, uow: UOWDep) -> UserProfile:
    service = AuthService(uow)
    return await service.get_user_profile(user)


@router.put("/profile-update", response_model=UserProfileUpdate)
async def profile_update(
    body_data: Annotated[UserProfileUpdate, Body()],
    user: UserDep,
    uow: UOWDep,
) -> UserProfileUpdate:
    service = AuthService(uow)
    return await service.update_user_profile(user, body_data)


@router.delete("/profile-delete", status_code=status.HTTP_204_NO_CONTENT)
async def profile_delete(user: UserDep, uow: UOWDep):
    service = AuthService(uow)
    return await service.delete_user_profile(user)
