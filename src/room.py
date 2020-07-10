# Implement a class to hold room information. This should have name and
# description attributes.
from termcolor import colored


class Room():
    def __init__(self, name: str, description: str, items: list) -> None:
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __repr__(self):
        return f"name: \"{self.name}\",\ndescription: \"{self.description}\"\n"
    
    def __str__(self):
        return \
            f"""
                name: \"{self.name}\",
                description: \"{self.description}\",
                Items: {self.items}
            """

    def give_up_item(self, item_name: str):
        room_items_names_list = [item.name for item in self.items]
        wanted_item_index = -1
        wanted_item = None

        if item_name in room_items_names_list:
            wanted_item_index = room_items_names_list.index(item_name)
            wanted_item = self.items.pop(wanted_item)
        
        return wanted_item
