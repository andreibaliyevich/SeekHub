from uuid import UUID
from schemas.users import UserDetails
from utilities.unit_of_work import AbstractUnitOfWork


class UsersService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def get_queryset(self, filters: dict):
        filters["disabled"] = False
        return await self.uow.user_repository.queryset(filters)

    async def get_user_by_id(self, id: UUID):
        async with self.uow:
            return await self.uow.user_repository.obj_by_id(id)

    async def update_user(self, id: UUID, data: UserDetails):
        user_dict = data.model_dump(exclude_unset=True)
        user = await self.uow.user_repository.update(id, user_dict)
        await self.uow.commit()
        await self.uow.session.refresh(user)
        return user

    async def delete_user(self, id: UUID):
        user_id = await self.uow.user_repository.delete(id)
        await self.uow.commit()
        return user_id
