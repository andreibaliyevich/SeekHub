from datetime import datetime
import uuid
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    DateTime,
    Relationship,
    text,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.users import Users
from models.likes import Likes


class Photos(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    file_url: str
    uploaded_at: datetime = Field(
        sa_column=Column(
            type_=DateTime,
            server_default=text("TIMEZONE('UTC', NOW())"),
            nullable=False,
        ),
    )
    is_public: bool = Field(default=True)

    owner_id: uuid.UUID = Field(foreign_key="users.id", ondelete="CASCADE")
    owner: "Users" = Relationship(back_populates="photos")

    likes: list["Users"] = Relationship(
        back_populates="photos_likes",
        link_model=Likes,
    )
