from datetime import date, datetime
import uuid
from pydantic import EmailStr
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    Date,
    DateTime,
    text,
)


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(max_length=254, unique=True, nullable=False)
    hashed_password: str = Field(max_length=255)
    disabled: bool = Field(default=True)
    date_joined: datetime = Field(
        sa_column=Column(
            type_=DateTime,
            server_default=text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
    )
    name: str = Field(max_length=64, index=True)
    birthday: date = Field(sa_type=Date)
    is_verified: bool = Field(default=False)
