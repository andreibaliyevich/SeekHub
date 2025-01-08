from pydantic import BaseModel, EmailStr


class UserToken(BaseModel):
    access_token: str
    token_type: str
    name: str


class TokenData(BaseModel):
    email: EmailStr | None = None
