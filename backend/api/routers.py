from api.auth import router as router_auth
from api.photos import router as router_photos
from api.users import router as router_users

all_routers = [
    router_auth,
    router_photos,
    router_users,
]
