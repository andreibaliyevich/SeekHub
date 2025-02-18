from uuid import UUID
from fastapi import UploadFile
from exceptions.auth import PermissionDeniedError
from exceptions.data import InvalidDataError
from models.users import Users
from schemas.photos import PhotoUpdate
from utilities.file_handler import FileHandler
from utilities.unit_of_work import AbstractUnitOfWork


class PhotosService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def _check_owner(self, photo_id: UUID, user: Users):
        photo = await self.uow.photos_repository.obj_by_id(photo_id)
        if photo.owner_id != user.id:
            raise PermissionDeniedError()
        return photo

    async def upload_photo(self, file: UploadFile, user: Users):
        allowed_extensions = {"jpg", "jpeg", "png", "gif"}
        photo_path = FileHandler().save_file(file, allowed_extensions)
        photo_dict = {
            "file_url": f"http://127.0.0.1:8000/photos/get/{photo_path}",
            "owner_id": user.id,
        }
        new_photo = await self.uow.photos_repository.add(photo_dict)
        await self.uow.commit()
        await self.uow.session.refresh(new_photo)
        return new_photo

    async def update_photo(self, id: UUID, data: PhotoUpdate, user: Users):
        photo = await self._check_owner(id, user)
        new_is_public = data.is_public if data.is_public is not None else photo.is_public
        new_is_primary = data.is_primary if data.is_primary is not None else photo.is_primary
        if not new_is_public and new_is_primary:
            raise InvalidDataError({
                "is_public": "A primary photo cannot be private.",
                "is_primary": "A private photo cannot be primary.",
            })
        if new_is_primary and not photo.is_primary:
            await self.uow.photos_repository.unset_primary_photos(user.id)
        photo_dict = data.model_dump(exclude_none=True)
        photo = await self.uow.photos_repository.update(id, photo_dict)
        await self.uow.commit()
        await self.uow.session.refresh(photo)
        return photo

    async def delete_photo(self, id: UUID, user: Users):
        photo = await self._check_owner(id, user)
        photo_path = photo.file_url.removeprefix("http://127.0.0.1:8000/photos/get/")
        FileHandler().delete_file(photo_path)
        photo_id = await self.uow.photos_repository.delete(id)
        await self.uow.commit()
        return photo_id
