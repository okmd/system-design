from collections import defaultdict

from splitwise.models.group import Group
from splitwise.services.group_service_interface import GroupServiceInterface


class GroupService(GroupServiceInterface):
    group_details = defaultdict()

    def add_group(self, id, name, members):
        group = Group(id, name, members)
        self.__class__.group_details[id] = group
        return group
