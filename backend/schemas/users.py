from datetime import date
from pydantic import BaseModel, EmailStr


class UsersBase(BaseModel):
    email: EmailStr
    name: str
    birthday: date
