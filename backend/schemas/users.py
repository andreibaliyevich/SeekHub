from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserList(BaseModel):
    id: UUID
    name: str


class UserDetails(BaseModel):
    id: UUID
    email: EmailStr
    date_joined: datetime
    name: str
    birthday: date
