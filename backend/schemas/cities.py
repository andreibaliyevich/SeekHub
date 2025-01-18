from uuid import UUID
from pydantic import BaseModel


class CityDetails(BaseModel):
    name: str
    country: str
    region: str | None = None
