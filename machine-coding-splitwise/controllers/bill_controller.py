class BillController(object):
    def __init__(self, bill_service):
        self.bill_service = bill_service

    def add_bill(self, id, group_id, amount, contributions, contributors):
        return self.bill_service.add_bill(id, group_id, amount, contributions, contributors)

    def get_user_balance(self, user_id):
        balance = 0
        for bill_id, bill in self.bill_service.bill_details.items():
            if user_id in bill.get_contributions():
                balance -= bill.get_contributions().get(user_id)
            if user_id in bill.get_contributors():
                balance += bill.get_contributors().get(user_id)
        return balance
