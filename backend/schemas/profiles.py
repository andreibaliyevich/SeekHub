from uuid import UUID
from pydantic import BaseModel, Field
from enums.profiles import (
    GenderType,
    BodyType,
    EthnicityType,
    RelationshipStatus,
    DrinkStatus,
    SmokeStatus,
    EducationLevel,
    OccupationType,
    AnnualIncomeLevel,
    NetWorthLevel,
    SeekingTags,
)
from schemas.cities import CityDetails


class ProfileDetails(BaseModel):
    gender: GenderType | None
    heading: str | None
    city: CityDetails | None
    height: int | None
    body_type: BodyType | None
    ethnicity: EthnicityType | None
    relationship_status: RelationshipStatus | None
    children: int | None
    drink: DrinkStatus | None
    smoke: SmokeStatus | None
    education: EducationLevel | None
    occupation: OccupationType | None
    annual_income: AnnualIncomeLevel | None
    net_worth: NetWorthLevel | None
    about: str | None
    gender_preference: GenderType | None
    age_preference_min: int | None
    age_preference_max: int | None
    seeking_tags: list[SeekingTags]


class ProfileUpdate(BaseModel):
    gender: GenderType | None = None
    heading: str | None = Field(default=None, max_length=50)
    city_id: UUID | None = None
    height: int | None = Field(default=None, ge=50, le=250)
    body_type: BodyType | None = None
    ethnicity: EthnicityType | None = None
    relationship_status: RelationshipStatus | None = None
    children: int | None = Field(default=None, ge=0, le=10)
    drink: DrinkStatus | None = None
    smoke: SmokeStatus | None = None
    education: EducationLevel | None = None
    occupation: OccupationType | None = None
    annual_income: AnnualIncomeLevel | None = None
    net_worth: NetWorthLevel | None = None
    about: str | None = Field(default=None, max_length=5000)
    gender_preference: GenderType | None = None
    age_preference_min: int | None = Field(default=None, ge=18, le=55)
    age_preference_max: int | None = Field(default=None, ge=18, le=55)
    seeking_tags: list[SeekingTags] | None = None
