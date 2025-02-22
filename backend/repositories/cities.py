from sqlmodel import select
from geoalchemy2 import functions as geo_func
from geoalchemy2.elements import WKTElement
from models.cities import Cities
from utilities.repository import SQLRepository


class CitiesRepository(SQLRepository):
    model = Cities

    async def search_by_name(self, query: str):
        stmt = select(self.model).filter(
            (Cities.name.ilike(f"%{query}%")) |
            (Cities.name_ascii.ilike(f"%{query}%"))
        )
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def city_by_location(self, latitude: float, longitude: float):
        user_location = WKTElement(f"POINT({longitude} {latitude})", srid=4326)
        stmt = select(Cities).order_by(
            geo_func.ST_Distance(Cities.location, user_location)
        ).limit(1)
        res = await self.session.execute(stmt)
        return res.scalars().first()
