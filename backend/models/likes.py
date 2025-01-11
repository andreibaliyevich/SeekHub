from datetime import datetime
from uuid import UUID
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    DateTime,
    text,
)


class Likes(SQLModel, table=True):
    photo_id: UUID = Field(
        foreign_key="photos.id",
        primary_key=True,
        ondelete="CASCADE",
    )
    user_id: UUID = Field(
        foreign_key="users.id",
        primary_key=True,
        ondelete="CASCADE",
    )
    created_at: datetime = Field(
        sa_column=Column(
            type_=DateTime,
            server_default=text("TIMEZONE('UTC', NOW())"),
            nullable=False,
        ),
    )
