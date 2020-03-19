# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_inventory(self):
        print("Your items: ")
        for item in self.items:
            print(item.name)

    def drop_item(self, item_name):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)
