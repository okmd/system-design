from abc import ABCMeta, abstractmethod


class GroupServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_group(self, id, name, members):
        pass
