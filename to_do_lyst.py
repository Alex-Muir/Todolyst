from item import Item

# A representation of a to-do list. 

class TodoList:
    """A representartion of a to-do list"""

    def __init__(self):
        """Initialize to-do list attributes"""

        self.items = []


    def add_item(self, desc):
        """Add an item to the to-do list"""

        item = Item(desc)
        self.items.append(item)


    def print_list(self):
        """Print the description and the status of itmes on the to-do list"""

        for item in self.items:
            print(f"description: {item.desc}")
            print(f"status: {item.status}\n\n")
