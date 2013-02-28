from unittest import TestCase

class TestStat(TestCase):
    def setUp(self):
        from warlord.stat import Stat
        self.stat = Stat()

    def test_default_value(self):
        self.assertEquals(self.stat.value, 0)

class TestHasMaxMixin(TestCase):
    def setUp(self):
        from warlord.stat import HasMaxMixin, Stat
        class MaxStat(HasMaxMixin, Stat):
            pass
        self.stat = MaxStat()

    def test_default_max_value(self):
        self.assertEquals(self.stat.max_value, 0)

    def test_cannot_exceed_max_value(self):
        self.stat.value += 1
        self.assertEquals(self.stat.value, 0)

class TestHasMinMixin(TestCase):
    def setUp(self):
        from warlord.stat import HasMinMixin, Stat
        class MinStat(HasMinMixin, Stat):
            pass
        self.stat = MinStat()

    def test_default_min_value(self):
        self.assertEquals(self.stat.min_value, 0)

    def test_cannot_exceed_min_value(self):
        self.stat.value -= 1
        self.assertEquals(self.stat.value, 0)
