from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import async_session_maker
from repositories.users import UsersRepository
from repositories.profiles import ProfilesRepository
from repositories.photos import PhotosRepository


class AbstractUnitOfWork(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def session(self) -> AsyncSession:
        raise NotImplementedError

    @property
    @abstractmethod
    def users_repository(self) -> UsersRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def profiles_repository(self) -> ProfilesRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def photos_repository(self) -> PhotosRepository:
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker
        self._session = None
        self._users_repository = None
        self._profiles_repository = None
        self._photos_repository = None

    @property
    def session(self) -> AsyncSession:
        if not self._session:
            raise ValueError("Session not initialized. Use UnitOfWork within a context manager.")
        return self._session

    @property
    def users_repository(self) -> UsersRepository:
        if not self._users_repository:
            self._users_repository = UsersRepository(self.session)
        return self._users_repository

    @property
    def profiles_repository(self) -> ProfilesRepository:
        if not self._profiles_repository:
            self._profiles_repository = ProfilesRepository(self.session)
        return self._profiles_repository

    @property
    def photos_repository(self) -> PhotosRepository:
        if not self._photos_repository:
            self._photos_repository = PhotosRepository(self.session)
        return self._photos_repository

    async def __aenter__(self):
        self._session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
