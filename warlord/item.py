class Item(object):
    def __init__(self):
        self.name = ''
        self.value = 0
        super(Item, self).__init__()

class IsUsableMixin(object):
    def use(self, *args, **kwargs):
        parent = super(IsUsableMixin, self)
        if hasattr(parent, 'use'):
            parent.use(*args, **kwargs)

class LimitedUsesMixin(IsUsableMixin):
    def __init__(self):
        self.uses = 0
        super(LimitedUsesMixin, self).__init__()

    def use(self, *args, **kwargs):
        self.uses -= 1
        super(LimitedUsesMixin, self).use(*args, **kwargs)

class StatChangingMixin(IsUsableMixin):
    def __init__(self):
        self.stats = {}
        super(StatChangingMixin, self).__init__()

    def use(self, target, *args, **kwargs):
        for stat_key, diff in self.stats.items():
            cur_value = getattr(target, stat_key)
            setattr(target, stat_key, cur_value + diff)
        super(StatChangingMixin, self).use(target, *args, **kwargs)
