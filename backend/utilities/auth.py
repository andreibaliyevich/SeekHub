from datetime import datetime, timedelta, timezone
import re
import jwt
from passlib.context import CryptContext
from config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(value: str) -> str:
    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    if not re.search(r"\d", value):
        raise ValueError("Password must contain at least one digit")

    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter")

    if not re.search(r"[@$!%*?&]", value):
        raise ValueError("Password must contain at least one special character (e.g. @, $, !, %, *, ?, &)")

    return value


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
