"""
Custom Exception for Invalid Form Data

This module defines a custom exception class for handling data validation errors in a FastAPI application. The exception provides a standardized way to respond to invalid data with detailed error information.

Classes:
    InvalidFormDataError:
        Raised when the submitted data is invalid or does not meet the expected validation criteria.

Details:
    - Automatically sets the HTTP status code to 400 (Bad Request).
    - Allows specifying detailed error messages in a dictionary or string format.
    - Includes custom headers for additional context.
"""

from fastapi import HTTPException, status


class InvalidDataError(HTTPException):
    """
    Exception raised when the submitted data is invalid.

    Attributes:
        detail (dict | str): Detailed error information, either as a dictionary with field-specific errors or as a general error message.
        status_code (int): HTTP status code for bad requests (400).
        headers (dict): HTTP headers containing additional context, such as "X-Error-Type".

    Args:
        detail (dict | str): Custom error details (default: "Invalid data.").

    Example:
        raise InvalidFormDataError({"field_name": "This field is required."})
    """
    def __init__(self, detail: dict | str = "Invalid data."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            headers={"X-Error-Type": "ValidationError"},
        )


class NotFoundError(HTTPException):
    """
    Exception raised when the requested resource is not found.

    Attributes:
        detail (str): Detailed error message describing the missing resource.
        status_code (int): HTTP status code for "Not Found" (404).
        headers (dict): HTTP headers providing additional context, such as "X-Error-Type".

    Args:
        detail (str): Custom error message (default: "Not Found.").

    Example:
        raise NotFoundError("User with ID 123 does not exist.")
        raise NotFoundError("File not found.")
    """
    def __init__(self, detail: str = "Not Found."):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
            headers={"X-Error-Type": "NotFound"},
        )
