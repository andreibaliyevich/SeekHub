"""
Custom Exception for Invalid Form Data

This module defines a custom exception class for handling form validation errors in a FastAPI application. The exception provides a standardized way to respond to invalid form data with detailed error information.

Classes:
    InvalidFormDataError:
        Raised when the submitted form data is invalid or does not meet the expected validation criteria.

Details:
    - Automatically sets the HTTP status code to 400 (Bad Request).
    - Allows specifying detailed error messages in a dictionary or string format.
    - Includes custom headers for additional context.
"""

from fastapi import HTTPException, status


class InvalidFormDataError(HTTPException):
    """
    Exception raised when the submitted form data is invalid.

    Attributes:
        detail (dict | str): Detailed error information, either as a dictionary with field-specific errors or as a general error message.
        status_code (int): HTTP status code for bad requests (400).
        headers (dict): HTTP headers containing additional context, such as "X-Error-Type".

    Args:
        detail (dict | str): Custom error details (default: "Invalid form data.").

    Example:
        raise InvalidFormDataError({"field_name": "This field is required."})
    """
    def __init__(self, detail: dict | str = "Invalid form data."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            headers={"X-Error-Type": "ValidationError"},
        )
