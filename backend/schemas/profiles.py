from uuid import UUID
from pydantic import BaseModel
from schemas.cities import CityDetails


class ProfileDetails(BaseModel):
    heading: str | None = None
    city: CityDetails | None = None


class ProfileUpdate(BaseModel):
    heading: str | None = None
    city_id: UUID | None = None
