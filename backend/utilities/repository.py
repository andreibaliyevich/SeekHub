"""
Repository Pattern for Data Access

This module implements the Repository pattern to abstract data access operations, providing a consistent interface for working with database models. It includes an abstract base class (`AbstractRepository`) and a concrete implementation (`SQLRepository`) designed for SQLModel and SQLAlchemy.

Classes:
    AbstractRepository:
        Abstract base class defining the contract for repository operations.

    SQLRepository:
        Concrete implementation of `AbstractRepository` for SQLModel, providing CRUD operations.

Methods:
    AbstractRepository:
        queryset(filters): Abstract method to retrieve objects based on filters.
        obj_by_id(id): Abstract method to retrieve a single object by its ID.
        add(data): Abstract method to add a new object.
        update(id, data): Abstract method to update an object by its ID.
        delete(id): Abstract method to delete an object by its ID.

    SQLRepository:
        queryset(filters): Retrieves objects matching the given filters.
        obj_by_id(id): Retrieves a single object by its ID.
        add(data): Adds a new object to the database.
        update(id, data): Updates an existing object by its ID.
        delete(id): Deletes an object by its ID.
"""

from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class AbstractRepository(ABC):
    """
    Abstract base class defining the contract for repository operations.

    Methods:
        queryset(filters): Abstract method to retrieve objects based on filters.
        obj_by_id(id): Abstract method to retrieve a single object by its ID.
        add(data): Abstract method to add a new object.
        update(id, data): Abstract method to update an object by its ID.
        delete(id): Abstract method to delete an object by its ID.
    """

    @abstractmethod
    async def queryset(self, **filters):
        """
        Retrieve objects based on provided filters.

        Args:
            **filters: Arbitrary keyword arguments for filtering the query.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    async def obj_by_id(self, id: UUID):
        """
        Retrieve a single object by its ID.

        Args:
            id (UUID): The unique identifier of the object.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    async def add(self, data: dict):
        """
        Add a new object to the database.

        Args:
            data (dict): The data used to create the object.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: UUID, data: dict):
        """
        Update an existing object by its ID.

        Args:
            id (UUID): The unique identifier of the object to be updated.
            data (dict): The data to update the object with.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: UUID):
        """
        Delete an object by its ID.

        Args:
            id (UUID): The unique identifier of the object to be deleted.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError


class SQLRepository(AbstractRepository):
    """
    Concrete implementation of AbstractRepository for SQLModel and SQLAlchemy.

    This class provides methods for common CRUD operations using SQLAlchemy and SQLModel.

    Attributes:
        model: The SQLModel class associated with the repository.
        session (AsyncSession): The SQLAlchemy session for database operations.
    """

    model = None

    def __init__(self, session: AsyncSession):
        """
        Initialize the repository with an asynchronous database session.

        Args:
            session (AsyncSession): The SQLAlchemy session to use for database operations.
        """
        self.session = session

    async def queryset(self, filters: dict):
        """
        Retrieve objects matching the given filters.

        Args:
            filters (dict): Key-value pairs used to filter the query.

        Returns:
            List: A list of objects that match the filters.
        """
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.scalars(stmt)
        return res.all()

    async def obj_by_id(self, id: UUID):
        """
        Retrieve a single object by its ID.

        Args:
            id (UUID): The unique identifier of the object.

        Returns:
            Object: The retrieved object.

        Raises:
            NoResultFound: If no object is found with the given ID.
        """
        obj = await self.session.get(self.model, id)
        if not obj:
            raise NoResultFound(f"{self.model.__name__} with ID {id} not found.")
        return obj

    async def add(self, data: dict):
        """
        Add a new object to the database.

        Args:
            data (dict): The data used to create the object.

        Returns:
            Object: The created object.
        """
        obj = self.model(**data)
        self.session.add(obj)
        return obj

    async def update(self, id: UUID, data: dict):
        """
        Update an existing object by its ID.

        Args:
            id (UUID): The unique identifier of the object to be updated.
            data (dict): The data to update the object with.

        Returns:
            Object: The updated object.
        """
        obj = await self.obj_by_id(id)
        obj.sqlmodel_update(data)
        self.session.add(obj)
        return obj

    async def delete(self, id: UUID):
        """
        Delete an object by its ID.

        Args:
            id (UUID): The unique identifier of the object to be deleted.

        Returns:
            UUID: The ID of the deleted object.
        """
        obj = await self.obj_by_id(id)
        await self.session.delete(obj)
        return id
