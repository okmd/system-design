class Group(object):
    def __init__(self, id: int = None, name: str = None, members: list = list()):
        """Initialize Group

        Args:
            id (int, optional): _description_. Defaults to None.
            name (str, optional): _description_. Defaults to None.
            members (list, optional): _description_. Defaults to list().
        """        
        self.id = id
        self.name = name
        self.members = members

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_members(self):
        return self.members

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_members(self, members):
        self.members = members
