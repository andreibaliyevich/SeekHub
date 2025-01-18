from models.profiles import Profiles
from utilities.repository import SQLRepository


class ProfilesRepository(SQLRepository):
    model = Profiles
