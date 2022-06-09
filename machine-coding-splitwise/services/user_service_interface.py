from abc import ABCMeta, abstractmethod


class UserServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self, id, name):
        pass
