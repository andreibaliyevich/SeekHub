from uuid import UUID
from pydantic import BaseModel


class CityDetails(BaseModel):
    id: UUID
    name: str
    country: str
    region: str | None = None
