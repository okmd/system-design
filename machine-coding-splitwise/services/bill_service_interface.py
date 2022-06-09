from abc import ABCMeta, abstractmethod


class BillServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_bill(self, id, group_id, amount, contributions, contibutors):
        pass
