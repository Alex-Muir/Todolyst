# An item that may be found on a to-do list. It contains a description and a 
# completion status

class Item:
    """A representation of an item on a to-do list"""

    def __init__(self, desc):
        """Initialize the Item attributes"""

        self.desc = desc
        self.status = "Incomplete"
