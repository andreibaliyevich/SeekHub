from utilities.unit_of_work import AbstractUnitOfWork


class CitiesService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def search_cities(self, query: str):
        return await self.uow.cities_repository.search_by_name(query)

    async def get_city_nearest(self, latitude: float, longitude: float):
        return await self.uow.cities_repository.city_by_location(latitude, longitude)
