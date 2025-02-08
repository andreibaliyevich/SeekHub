"""
Custom Exceptions for API Error Handling

This module defines custom exception classes for handling specific HTTP errors in a FastAPI application. These exceptions extend the `HTTPException` class from FastAPI, providing a more descriptive and reusable way to handle errors.

Classes:
    InvalidCredentialsError:
        Raised when the provided credentials (username or password) are invalid.

    PermissionDeniedError:
        Raised when a user attempts to access a resource without the necessary permissions.

Details:
    - Both exceptions automatically set the appropriate HTTP status codes and custom headers.
    - Designed to standardize error responses for authentication and authorization failures.
"""

from fastapi import HTTPException, status


class InvalidCredentialsError(HTTPException):
    """
    Exception raised when a user provides invalid credentials.

    Attributes:
        detail (str): A descriptive message explaining the error.
        status_code (int): HTTP status code for unauthorized access (401).
        headers (dict): HTTP headers containing additional context, such as "WWW-Authenticate".

    Args:
        detail (str): Custom error message (default: "Could not validate credentials.").

    Example:
        raise InvalidCredentialsError()
    """
    def __init__(self, detail: str = "Could not validate credentials."):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class PermissionDeniedError(HTTPException):
    """
    Exception raised when a user tries to access a resource without sufficient permissions.

    Attributes:
        detail (str): A descriptive message explaining the error.
        status_code (int): HTTP status code for forbidden access (403).
        headers (dict): HTTP headers containing additional context, such as "X-Error-Reason".

    Args:
        detail (str): Custom error message (default: "No permission to this resource.").

    Example:
        raise PermissionDeniedError()
    """
    def __init__(self, detail: str = "No permission to this resource."):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            headers={"X-Error-Reason": "Permission Denied"},
        )
