from uuid import UUID
from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.users import Users
    from models.cities import Cities


class Profiles(SQLModel, table=True):
    id: UUID = Field(
        primary_key=True,
        foreign_key="users.id",
        ondelete="CASCADE",
    )
    user: "Users" = Relationship(back_populates="profile")

    heading: str = Field(max_length=50, nullable=True)

    city_id: UUID | None = Field(
        default=None,
        foreign_key="cities.id",
        ondelete="SET NULL",
    )
    city: "Cities" = Relationship(back_populates="profiles")
