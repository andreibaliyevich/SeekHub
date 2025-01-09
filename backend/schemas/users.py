from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserList(BaseModel):
    id: UUID
    name: str
    is_verified: bool


class UserDetails(BaseModel):
    id: UUID
    email: EmailStr
    date_joined: datetime
    name: str
    birthday: date
    is_verified: bool
