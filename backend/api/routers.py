from api.auth import router as router_auth
from api.photos import router as router_photos
from api.users import router as router_users
from api.cities import router as router_cities

all_routers = [
    router_auth,
    router_photos,
    router_users,
    router_cities,
]
