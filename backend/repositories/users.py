from uuid import UUID
from pydantic import EmailStr
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import contains_eager, joinedload, selectinload
from sqlmodel import select
from models.users import Users
from models.photos import Photos
from models.profiles import Profiles
from utilities.repository import SQLRepository


class UsersRepository(SQLRepository):
    model = Users

    async def user_by_email(self, email: EmailStr):
        stmt = select(self.model).filter_by(email=email)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def user_with_primary_photo(self, id: UUID):
        stmt = (
            select(Users)
            .filter_by(id=id)
            .outerjoin(
                Photos,
                (Users.id == Photos.owner_id) & (Photos.is_primary == True),
            )
            .options(contains_eager(Users.photos))
        )
        res = await self.session.execute(stmt)
        user = res.unique().scalar_one_or_none()

        if user is None:
            raise NoResultFound(f"{self.model.__name__} with ID {id} not found.")
        return user

    async def user_profile(self, id: UUID):
        stmt = (
            select(Users)
            .filter_by(id=id)
            .options(
                joinedload(Users.profile).joinedload(Profiles.city),
                selectinload(Users.photos),
            )
        )
        res = await self.session.execute(stmt)
        user = res.scalar_one_or_none()

        if user is None:
            raise NoResultFound(f"{self.model.__name__} with ID {id} not found.")
        return user
