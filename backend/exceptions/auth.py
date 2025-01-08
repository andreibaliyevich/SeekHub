from fastapi import HTTPException, status


class InvalidCredentialsError(HTTPException):
    def __init__(self, detail: str = "Invalid username or password"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class InvalidFormDataError(HTTPException):
    def __init__(self, detail: dict | str = "Invalid form data"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )
