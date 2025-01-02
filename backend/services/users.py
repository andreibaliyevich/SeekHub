from uuid import UUID
from schemas.users import UsersBase
from utilities.unit_of_work import AbstractUnitOfWork


class UsersService:
    async def get_queryset(self, uow: AbstractUnitOfWork, filters: dict):
        async with uow:
            return await uow.user_repository.queryset(filters)

    async def get_user_by_id(self, uow: AbstractUnitOfWork, id: UUID):
        async with uow:
            return await uow.user_repository.obj_by_id(id)

    async def add_user(self, uow: AbstractUnitOfWork, data: UsersBase):
        user_dict = data.model_dump()
        async with uow:
            new_user = await uow.user_repository.add(user_dict)
            await uow.commit()
            await uow.session.refresh(new_user)
            return new_user

    async def update_user(self, uow: AbstractUnitOfWork, id: UUID, data: UsersBase):
        user_dict = data.model_dump(exclude_unset=True)
        async with uow:
            user = await uow.user_repository.update(id, user_dict)
            await uow.commit()
            await uow.session.refresh(user)
            return user

    async def delete_user(self, uow: AbstractUnitOfWork, id: UUID):
        async with uow:
            user_id = await uow.user_repository.delete(id)
            await uow.commit()
            return user_id
