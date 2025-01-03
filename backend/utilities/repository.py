from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class AbstractRepository(ABC):
    @abstractmethod
    async def queryset(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def obj_by_id(self, id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def add(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: UUID, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: UUID):
        raise NotImplementedError


class SQLRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def queryset(self, filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.scalars(stmt)
        return res.all()

    async def obj_by_id(self, id: UUID):
        obj = await self.session.get(self.model, id)
        if not obj:
            raise NoResultFound(f"{self.model.__name__} with ID {id} not found.")
        return obj

    async def add(self, data: dict):
        obj = self.model(**data)
        self.session.add(obj)
        return obj

    async def update(self, id: UUID, data: dict):
        obj = await self.obj_by_id(id)
        obj.sqlmodel_update(data)
        self.session.add(obj)
        return obj

    async def delete(self, id: UUID):
        obj = await self.obj_by_id(id)
        await self.session.delete(obj)
        return id
