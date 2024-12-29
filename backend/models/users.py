import uuid
from datetime import datetime
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    Date,
    DateTime,
    text,
)


class UserOrm(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    date_joined: datetime = Field(
        sa_column=Column(
            DateTime,
            server_default=text("TIMEZONE('utc', now())"),
        )
    )
    date_of_birth: datetime = Field(sa_column=Column(Date))
