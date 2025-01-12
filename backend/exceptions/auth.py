from fastapi import HTTPException, status


class InvalidCredentialsError(HTTPException):
    def __init__(self, detail: str = "Invalid username or password"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class PermissionDeniedError(HTTPException):
    def __init__(self, detail: str = "No permission to this resource"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            headers={"X-Error-Reason": "Permission Denied"},
        )
