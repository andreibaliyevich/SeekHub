import uuid
from datetime import date, datetime
from pydantic import EmailStr
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    String,
    Date,
    DateTime,
    text,
)


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(unique=True, nullable=False)
    name: str = Field(sa_type=String(64), index=True)
    date_joined: datetime = Field(
        sa_column=Column(
            type_=DateTime,
            server_default=text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
    )
    birthday: date = Field(sa_type=Date)
