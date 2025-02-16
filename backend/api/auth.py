from typing import Annotated
from fastapi import APIRouter, Body, Form, status
from api.dependencies import LoginFormDep, UserDep, UOWDep
from schemas.auth import (
    Token,
    RefreshToken,
    RegisterUser,
    RegisteredUser,
    UserPhoto,
    UserProfile,
    UserProfileUpdate,
    PasswordChange,
)
from services.auth import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/token", response_model=Token)
async def token(form_data: LoginFormDep, uow: UOWDep) -> Token:
    service = AuthService(uow)
    return await service.authenticate_user(form_data.username, form_data.password)


@router.post("/refresh", response_model=Token)
async def refresh(
    body_data: Annotated[RefreshToken, Body()],
    uow: UOWDep,
) -> Token:
    service = AuthService(uow)
    return await service.refresh_tokens(body_data)


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


@router.get("/user", response_model=UserPhoto)
async def user(user: UserDep, uow: UOWDep) -> UserPhoto:
    service = AuthService(uow)
    return await service.get_user_with_primary_photo(user)


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


@router.post("/password-change", status_code=status.HTTP_204_NO_CONTENT)
async def password_change(
    form_data: Annotated[PasswordChange, Form()],
    user: UserDep,
    uow: UOWDep,
):
    service = AuthService(uow)
    return await service.change_password(user, form_data)


@router.delete("/user-delete", status_code=status.HTTP_204_NO_CONTENT)
async def user_delete(user: UserDep, uow: UOWDep):
    service = AuthService(uow)
    return await service.delete_user(user)
