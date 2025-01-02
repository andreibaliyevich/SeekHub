from models.users import Users
from utilities.repository import SQLRepository


class UsersRepository(SQLRepository):
    model = Users
