from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Form, Request
from api.dependencies import UOWDep
from schemas.users import UsersBase
from services.users import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/list")
async def user_list(request: Request, uow: UOWDep):
    service = UsersService(uow)
    return await service.get_queryset(dict(request.query_params))


@router.post("/add")
async def add_user(data: Annotated[UsersBase, Form()], uow: UOWDep):
    service = UsersService(uow)
    return await service.add_user(data)


@router.get("/get/{id}")
async def get_user(id: UUID, uow: UOWDep):
    service = UsersService(uow)
    return await service.get_user_by_id(id)


@router.put("/update/{id}")
async def update_user(id: UUID, data: Annotated[UsersBase, Form()], uow: UOWDep):
    service = UsersService(uow)
    return await service.update_user(id, data)


@router.delete("/delete/{id}")
async def add_user(id: UUID, uow: UOWDep):
    service = UsersService(uow)
    return await service.delete_user(id)
