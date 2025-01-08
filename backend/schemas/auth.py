from datetime import date
from pydantic import BaseModel, EmailStr


class UserToken(BaseModel):
    access_token: str
    token_type: str
    name: str


class TokenData(BaseModel):
    email: EmailStr | None = None


class RegisterUser(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    name: str
    birthday: date
