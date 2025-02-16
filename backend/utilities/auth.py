"""
Utility Functions for Password Management and JWT Token Generation

This module provides utility functions for managing passwords and generating JSON Web Tokens (JWT) for authentication.

Functions:
    validate_password(value: str) -> str:
        Validates a password against defined security rules (minimum length, digits, uppercase letters, and special characters).

    verify_password(plain_password: str, hashed_password: str) -> bool:
        Verifies a plaintext password against a hashed password.

    get_password_hash(password: str) -> str:
        Hashes a plaintext password using bcrypt.

    create_tokens(data: dict) -> tuple[str, str]:
        Generates an access token and a refresh token using JWT.

    decode_token(token: str, refresh: bool = False) -> str | None:
        Decodes a JWT token and verifies its validity.
"""

from datetime import datetime, timedelta, timezone
import re
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from config import settings
from db.cache import redis_client


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(value: str) -> str:
    """
    Validates a password against the following rules:
        - Must be at least 8 characters long.
        - Must contain at least one digit.
        - Must contain at least one uppercase letter.
        - Must contain at least one special character (e.g., @, $, !, %, *, ?, &).

    Args:
        value (str): The password to validate.

    Raises:
        ValueError: If the password does not meet any of the security rules.

    Returns:
        str: The validated password.
    """
    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if not re.search(r"\d", value):
        raise ValueError("Password must contain at least one digit.")

    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not re.search(r"[@$!%*?&]", value):
        raise ValueError("Password must contain at least one special character (e.g. @, $, !, %, *, ?, &).")

    return value


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the plaintext password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hashes a plaintext password using the bcrypt hashing algorithm.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


async def create_tokens(data: dict) -> tuple[str, str]:
    """
    Generates an access token and a refresh token using JWT.

    The access token expires in a short period (e.g., minutes), while the refresh token lasts longer (e.g., days).
    The refresh token is stored in Redis to ensure security and prevent reuse after invalidation.

    Args:
        data (dict): The payload containing user information (e.g., user ID) to be included in the tokens.

    Returns:
        tuple[str, str]: A tuple containing the access token and refresh token.
    """
    now = datetime.now(timezone.utc)
    access_token = jwt.encode(
        {**data, "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    refresh_token = jwt.encode(
        {**data, "exp": now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)},
        settings.REFRESH_SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    await redis_client.setex(
        name=f"refresh:{data['sub']}",
        time=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        value=refresh_token,
    )
    return access_token, refresh_token


async def decode_token(token: str, refresh: bool = False) -> str | None:
    """
    Decodes a JWT token and verifies its validity.

    If the token is a refresh token, its presence in Redis is also checked to prevent reuse after invalidation.

    Args:
        token (str): The JWT token to decode.
        refresh (bool, optional): Whether the token is a refresh token. Defaults to False.

    Returns:
        str | None: The user ID if the token is valid, otherwise None.
    """
    secret_key = settings.REFRESH_SECRET_KEY if refresh else settings.SECRET_KEY

    try:
        payload = jwt.decode(token, secret_key, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
    except InvalidTokenError:
        return None

    if refresh:
        stored_refresh_token = await redis_client.get(f"refresh:{user_id}")
        if not stored_refresh_token or stored_refresh_token.decode() != token:
            return None

    return user_id
