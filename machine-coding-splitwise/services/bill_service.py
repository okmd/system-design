from collections import defaultdict

from splitwise.models.bill import Bill
from splitwise.services.bill_service_interface import BillServiceInterface


class BillService(BillServiceInterface):
    bill_details = defaultdict()

    def add_bill(self, id, group_id, amount, contributions, contributors):
        bill = Bill(id, group_id, amount, contributions, contributors)
        self.__class__.bill_details[id] = bill
        return bill
