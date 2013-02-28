class Stat(object):
    def __init__(self):
        self._value = 0
        super(Stat, self).__init__()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class HasMaxMixin(object):
    def __init__(self):
        self.max_value = 0
        super(HasMaxMixin, self).__init__()

    @property
    def value(self):
        return super(HasMaxMixin, self).value

    @value.setter
    def value(self, new_value):
        value = min(new_value, self.max_value)

class HasMinMixin(object):
    def __init__(self):
        self.min_value = 0
        super(HasMinMixin, self).__init__()

    @property
    def value(self):
        return super(HasMinMixin, self).value

    @value.setter
    def value(self, new_value):
        value = max(new_value, self.min_value)
