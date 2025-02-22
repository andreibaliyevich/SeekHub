"""
Unit of Work Pattern for Managing Database Transactions

This module defines an abstraction and implementation of the Unit of Work (UoW) pattern to manage database transactions effectively. It provides a context-managed environment for handling database operations, ensuring atomicity and consistency.

Classes:
    AbstractUnitOfWork:
        Abstract base class for the Unit of Work pattern.

    UnitOfWork:
        Concrete implementation of the Unit of Work pattern.

Methods:
    AbstractUnitOfWork:
        __init__(): Abstract method to initialize the UoW.
        session: Abstract property for accessing the database session.
        users_repository: Abstract property for accessing the UsersRepository.
        profiles_repository: Abstract property for accessing the ProfilesRepository.
        photos_repository: Abstract property for accessing the PhotosRepository.
        cities_repository: Abstract property for accessing the CitiesRepository.
        __aenter__(): Abstract method for entering an async context.
        __aexit__(): Abstract method for exiting an async context.
        commit(): Abstract method for committing a transaction.
        rollback(): Abstract method for rolling back a transaction.

    UnitOfWork:
        __init__(): Initializes the UoW with repositories and session management.
        session: Property to lazily initialize and return the database session.
        users_repository: Property to lazily initialize and return the UsersRepository.
        profiles_repository: Property to lazily initialize and return the ProfilesRepository.
        photos_repository: Property to lazily initialize and return the PhotosRepository.
        cities_repository: Property to lazily initialize and return the CitiesRepository.
        __aenter__(): Enters the context manager, creating a database session.
        __aexit__(): Exits the context manager, rolling back on exception and closing the session.
        commit(): Commits the current transaction.
        rollback(): Rolls back the current transaction.
"""

from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import async_session_maker
from repositories.users import UsersRepository
from repositories.profiles import ProfilesRepository
from repositories.photos import PhotosRepository
from repositories.cities import CitiesRepository


class AbstractUnitOfWork(ABC):
    """
    Abstract base class for the Unit of Work pattern.

    This class defines the contract for implementing a Unit of Work, managing repositories and database transactions.
    """

    @abstractmethod
    def __init__(self):
        """
        Abstract method to initialize the Unit of Work.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def session(self) -> AsyncSession:
        """
        Abstract property to access the database session.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def users_repository(self) -> UsersRepository:
        """
        Abstract property to access the UsersRepository.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def profiles_repository(self) -> ProfilesRepository:
        """
        Abstract property to access the ProfilesRepository.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def photos_repository(self) -> PhotosRepository:
        """
        Abstract property to access the PhotosRepository.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def cities_repository(self) -> CitiesRepository:
        """
        Abstract property to access the CitiesRepository.
        """
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        """
        Abstract method for entering an async context.
        """
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Abstract method for exiting an async context.
        """
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        """
        Abstract method for committing the current transaction.
        """
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        """
        Abstract method for rolling back the current transaction.
        """
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    """
    Concrete implementation of the Unit of Work pattern.

    This class manages database transactions and provides access to repositories.
    """

    def __init__(self):
        """
        Initializes the Unit of Work.

        Attributes:
            session_factory: A callable for creating an async database session.
            _session: An instance of AsyncSession, lazily initialized.
            _users_repository: An instance of UsersRepository, lazily initialized.
            _profiles_repository: An instance of ProfilesRepository, lazily initialized.
            _photos_repository: An instance of PhotosRepository, lazily initialized.
            _cities_repository: An instance of CitiesRepository, lazily initialized.
        """
        self.session_factory = async_session_maker
        self._session = None
        self._users_repository = None
        self._profiles_repository = None
        self._photos_repository = None
        self._cities_repository = None

    @property
    def session(self) -> AsyncSession:
        """
        Lazily initializes and returns the database session.

        Returns:
            AsyncSession: The database session.

        Raises:
            ValueError: If accessed outside a context manager.
        """
        if not self._session:
            raise ValueError("Session not initialized. Use UnitOfWork within a context manager.")
        return self._session

    @property
    def users_repository(self) -> UsersRepository:
        """
        Lazily initializes and returns the UsersRepository.
        """
        if not self._users_repository:
            self._users_repository = UsersRepository(self.session)
        return self._users_repository

    @property
    def profiles_repository(self) -> ProfilesRepository:
        """
        Lazily initializes and returns the ProfilesRepository.
        """
        if not self._profiles_repository:
            self._profiles_repository = ProfilesRepository(self.session)
        return self._profiles_repository

    @property
    def photos_repository(self) -> PhotosRepository:
        """
        Lazily initializes and returns the PhotosRepository.
        """
        if not self._photos_repository:
            self._photos_repository = PhotosRepository(self.session)
        return self._photos_repository

    @property
    def cities_repository(self) -> CitiesRepository:
        """
        Lazily initializes and returns the CitiesRepository.
        """
        if not self._cities_repository:
            self._cities_repository = CitiesRepository(self.session)
        return self._cities_repository

    async def __aenter__(self):
        """
        Enters the context manager, creating a database session.

        Returns:
            UnitOfWork: The current instance of UnitOfWork.
        """
        self._session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exits the context manager, rolling back on exception and closing the session.

        Args:
            exc_type: The type of exception, if any.
            exc_val: The value of the exception, if any.
            exc_tb: The traceback of the exception, if any.
        """
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        """
        Commits the current transaction.
        """
        await self.session.commit()

    async def rollback(self):
        """
        Rolls back the current transaction.
        """
        await self.session.rollback()
