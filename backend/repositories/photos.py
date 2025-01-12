from uuid import UUID
from sqlmodel import update
from models.photos import Photos
from utilities.repository import SQLRepository


class PhotosRepository(SQLRepository):
    model = Photos

    async def unset_primary_photos(self, user_id: UUID):
        await self.session.execute(
            update(self.model)
            .filter_by(owner_id=user_id, is_primary=True)
            .values(is_primary=False)
        )
