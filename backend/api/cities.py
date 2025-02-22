from typing import Annotated
from fastapi import APIRouter, Query
from api.dependencies import UOWDep
from schemas.cities import CityDetails
from services.cities import CitiesService


router = APIRouter(
    prefix="/cities",
    tags=["Cities"],
)


@router.get("/search", response_model=list[CityDetails])
async def cities_search(
    query: Annotated[str, Query(min_length=3, max_length=150)],
    uow: UOWDep,
) -> list[CityDetails]:
    service = CitiesService(uow)
    return await service.search_cities(query)


@router.get("/nearest", response_model=CityDetails)
async def city_nearest(
    latitude: Annotated[float, Query()],
    longitude: Annotated[float, Query()],
    uow: UOWDep,
) -> CityDetails:
    service = CitiesService(uow)
    return await service.get_city_nearest(latitude, longitude)
