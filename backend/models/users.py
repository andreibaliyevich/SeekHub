import uuid
from datetime import date, datetime
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
    name: str = Field(max_length=64, index=True)
    date_joined: datetime = Field(
        sa_column=Column(
            type_=DateTime,
            server_default=text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
    )
    birthday: date = Field(sa_type=Date)
