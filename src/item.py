class Item:
    def __init__(self, name, description):
        self.name = name


class Food(Item):
    def __init__(self, name, description, heal_amount):
        self.name = name
        self.description = description
        self.heal_amount = heal_amount


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
