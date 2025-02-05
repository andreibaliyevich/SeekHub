from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class PhotoList(BaseModel):
    id: UUID
    file_url: str
    uploaded_at: datetime
    is_public: bool
    is_primary: bool


class PhotoUpdate(BaseModel):
    is_public: bool | None = None
    is_primary: bool | None = None


class PhotoListRead(BaseModel):
    file_url: str
    uploaded_at: datetime
    is_public: bool
    is_primary: bool
