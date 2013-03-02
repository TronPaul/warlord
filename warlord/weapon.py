from item import Item, LimitedUsesMixin

class Weapon(LimitedUsesMixin, Item):
    def __init__(self):
        super(Weapon, self).__init__()
        self.weight = 0
        self.accuracy = 0
