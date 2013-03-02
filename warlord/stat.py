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

class HasStats(object):
    _stat_prefix = '_stat_'
    def __getattr__(self, name):
        if hasattr(self, self._stat_prefix + name):
            stat = self.get_stat(name)
            return stat.value
        if name.startswith('max_') or name.startswith('min_'):
            val_type = name[:4]
            name = name[4:]
            return getattr(self.get_stat(name), val_type + 'value')
        return super(HasStats, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if hasattr(self, self._stat_prefix + name):
            stat = self.get_stat(name)
            stat.value = value
            return
        return super(HasStats, self).__setattr__(name, value)

    def has_stat(self, name):
        return hasattr(self, self._stat_prefix + name)

    def get_stat(self, name):
        return self.__dict__[self._stat_prefix + name]

    def add_stat(self, name, min_value=None, max_value=None):
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
        setattr(self, self._stat_prefix + name, stat)
