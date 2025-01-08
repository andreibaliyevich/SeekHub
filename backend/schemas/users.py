from datetime import date
from pydantic import BaseModel, EmailStr


class UsersBase(BaseModel):
    email: EmailStr
    password: str
    name: str
    birthday: date
