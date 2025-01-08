from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Form, Request, status
from api.dependencies import UOWDep
from schemas.users import UserList, UserDetails
from services.users import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[UserList])
async def user_list(request: Request, uow: UOWDep) -> list[UserList]:
    service = UsersService(uow)
    return await service.get_queryset(dict(request.query_params))


@router.get("/{id}", response_model=UserDetails)
async def user_details(id: UUID, uow: UOWDep) -> UserDetails:
    service = UsersService(uow)
    return await service.get_user_by_id(id)


@router.put("/{id}")
async def update_user(id: UUID, data: Annotated[UserDetails, Form()], uow: UOWDep):
    service = UsersService(uow)
    return await service.update_user(id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: UUID, uow: UOWDep):
    service = UsersService(uow)
    return await service.delete_user(id)
