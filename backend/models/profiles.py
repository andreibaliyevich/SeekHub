from uuid import UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)
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

    gender: GenderType | None = Field(default=None)
    heading: str = Field(max_length=50, nullable=True)

    city_id: UUID | None = Field(
        default=None,
        foreign_key="cities.id",
        ondelete="SET NULL",
    )
    city: "Cities" = Relationship(back_populates="profiles")

    height: int | None = Field(default=None, ge=50, le=250)
    body_type: BodyType | None = Field(default=None)
    ethnicity: EthnicityType | None = Field(default=None)
    relationship_status: RelationshipStatus | None = Field(default=None)
    children: int | None = Field(default=None, ge=0, le=10)
    drink: DrinkStatus | None = Field(default=None)
    smoke: SmokeStatus | None = Field(default=None)
    education: EducationLevel | None = Field(default=None)
    occupation: OccupationType | None = Field(default=None)
    annual_income: AnnualIncomeLevel | None = Field(default=None)
    net_worth: NetWorthLevel | None = Field(default=None)
    about: str = Field(max_length=5000, nullable=True)

    gender_preference: GenderType | None = Field(default=None)
    age_preference_min: int | None = Field(default=None, ge=18, le=55)
    age_preference_max: int | None = Field(default=None, ge=18, le=55)
    seeking_tags: list[SeekingTags] = Field(
        default_factory=list,
        sa_type=JSONB,
    )
