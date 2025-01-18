from uuid import UUID, uuid4
from geoalchemy2 import Geometry
from sqlmodel import (
    SQLModel,
    Field,
    Column,
)


class Cities(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=150, index=True)
    name_ascii: str = Field(max_length=150, index=True)
    location: str = Field(sa_column=Column(
        Geometry(geometry_type="POINT", srid=4326),
    ))
    country: str = Field(max_length=100)
    country_code: str = Field(max_length=3, index=True)
    region: str = Field(max_length=150, nullable=True)
