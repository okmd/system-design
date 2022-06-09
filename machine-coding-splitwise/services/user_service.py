from collections import defaultdict

from splitwise.models.user import User
from splitwise.services.user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    user_details = defaultdict()

    def add_user(self, id, name):
        user = User(id, name)
        self.__class__.user_details[id] = user
        return user
