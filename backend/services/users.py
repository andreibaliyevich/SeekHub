from uuid import UUID
from utilities.unit_of_work import AbstractUnitOfWork


class UsersService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def get_queryset(self, filters: dict):
        filters["is_active"] = True
        return await self.uow.user_repository.queryset(filters)

    async def get_user_by_id(self, id: UUID):
        async with self.uow:
            return await self.uow.user_repository.obj_by_id(id)
