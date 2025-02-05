from pathlib import Path
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, File, Form, status, UploadFile
from fastapi.responses import FileResponse
from api.dependencies import UserDep, UOWDep
from exceptions.auth import PermissionDeniedError
from exceptions.data import NotFoundError
from schemas.photos import PhotoList, PhotoUpdate
from services.photos import PhotosService


router = APIRouter(
    prefix="/photos",
    tags=["Photos"],
)


@router.post(
        "/upload",
        response_model=PhotoList,
        status_code=status.HTTP_201_CREATED,
)
async def photo_upload(
    file: Annotated[UploadFile, File()],
    user: UserDep,
    uow: UOWDep,
) -> PhotoList:
    service = PhotosService(uow)
    return await service.upload_photo(file, user)


@router.put("/update/{id}", response_model=PhotoUpdate)
async def photo_update(
    id: UUID,
    form_data: Annotated[PhotoUpdate, Form()],
    user: UserDep,
    uow: UOWDep,
) -> PhotoUpdate:
    service = PhotosService(uow)
    return await service.update_photo(id, form_data, user)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def photo_delete(id: UUID, user: UserDep, uow: UOWDep):
    service = PhotosService(uow)
    return await service.delete_photo(id, user)


@router.get("/get/{file_path:path}")
async def get_photo(file_path: str):
    base_dir = Path("media").resolve()
    full_path = Path(file_path).resolve()

    if not str(full_path).startswith(str(base_dir)):
        raise PermissionDeniedError
    if not full_path.is_file():
        raise NotFoundError(detail="File not found.")

    return FileResponse(full_path)
