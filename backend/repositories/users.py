from uuid import UUID
from pydantic import EmailStr
from sqlalchemy.orm import joinedload, selectinload
from sqlmodel import select
from models.users import Users
from models.profiles import Profiles
from utilities.repository import SQLRepository


class UsersRepository(SQLRepository):
    model = Users

    async def obj_by_email(self, email: EmailStr):
        stmt = select(self.model).filter_by(email=email)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def get_full_profile(self, id: UUID):
        stmt = (
            select(Users)
            .filter_by(id=id)
            .options(
                joinedload(Users.profile).joinedload(Profiles.city),
                selectinload(Users.photos),
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
