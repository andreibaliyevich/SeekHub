from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr
from schemas.photos import PhotoList
from schemas.profiles import ProfileDetails


class UserList(BaseModel):
    id: UUID
    name: str
    is_verified: bool


class UserDetails(BaseModel):
    date_joined: datetime
    name: str
    birthday: date
    is_verified: bool

    profile: ProfileDetails
    photos: list[PhotoList]
