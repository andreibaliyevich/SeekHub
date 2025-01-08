from pydantic import EmailStr
from sqlmodel import select
from models.users import Users
from utilities.repository import SQLRepository


class UsersRepository(SQLRepository):
    model = Users

    async def obj_by_email(self, email: EmailStr):
        stmt = select(self.model).filter_by(email=email)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()
