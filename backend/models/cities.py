from uuid import UUID, uuid4
from geoalchemy2 import Geometry
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    Relationship
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.profiles import Profiles


class Cities(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=150, index=True)
    name_ascii: str = Field(max_length=150, index=True)
    location: str = Field(sa_column=Column(
        Geometry(geometry_type="POINT", srid=4326),
        index=True,
    ))
    country: str = Field(max_length=100)
    country_code: str = Field(max_length=3, index=True)
    region: str = Field(max_length=150, nullable=True)

    profiles: list["Profiles"] = Relationship(back_populates="city")
