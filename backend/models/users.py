from datetime import date, datetime
import uuid
from pydantic import EmailStr
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    Date,
    DateTime,
    Relationship,
    text,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.profiles import Profiles
    from models.photos import Photos
from models.likes import Likes


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(max_length=254, unique=True, nullable=False)
    hashed_password: str = Field(max_length=255)
    is_active: bool = Field(default=False)
    date_joined: datetime = Field(sa_column=Column(
        type_=DateTime,
        server_default=text("TIMEZONE('UTC', NOW())"),
        nullable=False,
    ))
    name: str = Field(max_length=64, index=True)
    birthday: date = Field(sa_type=Date)
    is_verified: bool = Field(default=False)

    profile: "Profiles" = Relationship(back_populates="user")
    photos: list["Photos"] = Relationship(
        back_populates="owner",
        cascade_delete=True,
    )
    photos_likes: list["Photos"] = Relationship(
        back_populates="likes",
        link_model=Likes,
    )
