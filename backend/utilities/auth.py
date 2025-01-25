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

    create_access_token(data: dict) -> str:
        Generates a JWT access token with an expiration date based on the provided data.
"""

from datetime import datetime, timedelta, timezone
import re
import jwt
from passlib.context import CryptContext
from config import settings


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
        raise ValueError("Password must be at least 8 characters long")

    if not re.search(r"\d", value):
        raise ValueError("Password must contain at least one digit")

    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter")

    if not re.search(r"[@$!%*?&]", value):
        raise ValueError("Password must contain at least one special character (e.g. @, $, !, %, *, ?, &)")

    return value


def verify_password(plain_password: str, hashed_password: str):
    """
    Verifies a plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the plaintext password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """
    Hashes a plaintext password using the bcrypt hashing algorithm.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """
    Generates a JWT access token with an expiration date.

    Args:
        data (dict): The payload to include in the token.

    Returns:
        str: The encoded JWT access token.

    Notes:
        - The expiration date is determined by the `ACCESS_TOKEN_EXPIRE_DAYS` setting.
        - The token is signed using the `SECRET_KEY` and `ALGORITHM` defined in the settings.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
