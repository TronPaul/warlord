class ItemOutOfUsesError(ValueError):
    pass

class Item(object):
    equipable = False
    def __init__(self):
        self.name = ''
        self.value = 0
        self.owner = None
        super(Item, self).__init__()

class IsUsableMixin(object):
    def use(self, *args, **kwargs):
        pass

class LimitedUseMixin(IsUsableMixin):
    def __init__(self):
        self.uses = 0
        super(LimitedUseMixin, self).__init__()

    def use(self, *args, **kwargs):
        if self.uses < 1:
            raise ItemOutOfUsesError
        super(LimitedUseMixin, self).use(*args, **kwargs)
        self.uses -= 1

class StatChangingMixin(IsUsableMixin):
    def __init__(self):
        self.stats = {}
        super(StatChangingMixin, self).__init__()

    def use(self, target, *args, **kwargs):
        for stat, modifier in self.stats.items():
            cur_value = getattr(target, stat)
            setattr(target, stat, cur_value + modifier)
        super(StatChangingMixin, self).use(target, *args, **kwargs)

class LimitedUseStatChangingItem(LimitedUseMixin, StatChangingMixin, Item):
    pass
