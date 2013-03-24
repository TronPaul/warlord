class Effect(object):
    def __init__(self):
        self.target = None
        self.stats = {}

    def apply_effect(self):
        for stat, modifier in self.stats:
            cur_value = getattr(self.target, stat)
            setattr(self.target, stat, cur_value + modifier)

    def remove_effect(self):
        for stat, modifier in self.stats:
            cur_value = getattr(self.target, stat)
            setattr(self.target, stat, cur_value - modifier)

class RecurringEffect(Effect):
    def __init__(self):
        super(RecurringEffects, self).__init__()
        self.duration = 0

    def apply_effect(self):
        if self.duration < 1:
            raise EffectOutOfDurationError
        super(RecurringEffect, self).apply_effect()
        self.duration -= 1

class HasEffects(object):
    def __init__(self):
        super(HasEffects, self).__init__()
        self.effects = []

    def add_effect(self, effect):
        self.effects.append(effect)
        effect.target = self

    def remove_effect(self, effect):
        self.effects.remove(effect)
        effect.target = None
