from typing import Any
from datetime import date, datetime
from typing import Annotated, Self
from uuid import UUID
from pydantic import (
    AfterValidator,
    BaseModel,
    EmailStr,
    model_validator,
)
from schemas.photos import PhotoList
from schemas.profiles import ProfileDetails, ProfileUpdate
from utilities.auth import validate_password


class UserToken(BaseModel):
    access_token: str
    token_type: str
    name: str


class TokenData(BaseModel):
    id: UUID | None = None


class RegisterUser(BaseModel):
    email: EmailStr
    password: Annotated[str, AfterValidator(validate_password)]
    confirm_password: str
    name: str
    birthday: date

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match.")
        return self


class RegisteredUser(BaseModel):
    id: UUID
    email: EmailStr
    date_joined: datetime
    name: str
    birthday: date


class PasswordChange(BaseModel):
    current_password: str
    new_password: Annotated[str, AfterValidator(validate_password)]
    confirm_new_password: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.new_password != self.confirm_new_password:
            raise ValueError("New passwords do not match.")
        return self


class UserProfile(BaseModel):
    id: UUID
    email: EmailStr
    date_joined: datetime
    name: str
    birthday: date
    is_verified: bool

    profile: ProfileDetails
    photos: list[PhotoList]


class UserProfileUpdate(BaseModel):
    name: str | None = None
    birthday: date | None = None

    profile: ProfileUpdate | None = None

    @model_validator(mode="before")
    @classmethod
    def check_at_least_one_field(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if not any(data.values()):
                raise ValueError("At least one field must be provided.")
        return data
