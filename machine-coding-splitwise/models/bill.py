from collections import defaultdict


class Bill(object):
    def __init__(self, id: int = None, group_id: int = None, amount: float = None, contributions: defaultdict = defaultdict(), contributors: defaultdict = defaultdict()) -> None:
        """_summary_

        Args:
            id (int, optional): _description_. Defaults to None.
            group_id (int, optional): _description_. Defaults to None.
            amount (float, optional): _description_. Defaults to None.
            contributions (defaultdict, optional): _description_. Defaults to defaultdict().
            contributors (defaultdict, optional): _description_. Defaults to defaultdict().
        """
        self.id = id
        self.group_id = group_id
        self.amount = amount
        self.contributions = contributions
        self.contributors = contributors

    def get_id(self) -> int:
        """Get bill id of the current bill.

        Returns:
            int: return the bill id.
        """
        return self.id

    def get_group_id(self):
        return self.group_id

    def get_amount(self):
        return self.amount

    def get_contributions(self):
        return self.contributions

    def get_contributors(self):
        return self.contributors

    def set_id(self, id):
        self.id = id

    def set_group_id(self, group_id):
        self.group_id = group_id

    def set_amount(self, amount):
        self.amount = amount

    def set_contributions(self, contributions):
        self.contributions = contributions

    def set_contributors(self, contributors):
        self.contributors = contributors
