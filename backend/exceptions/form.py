from fastapi import HTTPException, status


class InvalidFormDataError(HTTPException):
    def __init__(self, detail: dict | str = "Invalid form data"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )
