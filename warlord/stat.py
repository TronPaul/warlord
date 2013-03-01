class Stat(object):
    def __init__(self):
        self.value = 0
        super(Stat, self).__init__()

class HasMaxMixin(object):
    def __init__(self):
        self.max_value = 0
        super(HasMaxMixin, self).__init__()

    def __setattr__(self, name, value):
        if name == 'value':
            value = min(value, self.max_value)
        super(HasMaxMixin, self).__setattr__(name, value)

class HasMinMixin(object):
    def __init__(self):
        self.min_value = 0
        super(HasMinMixin, self).__init__()

    def __setattr__(self, name, value):
        if name == 'value':
            value = max(value, self.min_value)
        super(HasMinMixin, self).__setattr__(name, value)

class MaxStat(HasMaxMixin, Stat):
    pass

class MinStat(HasMinMixin, Stat):
    pass

class MinMaxStat(HasMinMixin, HasMaxMixin, Stat):
    pass

class StatManager(object):
    def __init__(self):
        self.stats = {}

    def __getitem__(self, key):
        if key.startswith('min_'):
            key = key[4:]
            return self.stats[key].min_value
        elif key.startswith('max_'):
            key = key[4:]
            return self.stats[key].max_value
        return self.stats[key].value

    def __setitem__(self, key, value):
        self.stats[key].value = value

    def add_stat(self, name, max_value=None, min_value=None):
        if min_value is not None and max_value is not None:
            stat = MinMaxStat()
            stat.min_value = min_value
            stat.max_value = max_value
        elif max_value is not None:
            stat = MaxStat()
            stat.max_value = max_value
        elif min_value is not None:
            stat = MinStat()
            stat.min_value = min_value
        else:
            stat = Stat()
        self.stats[name] = stat
