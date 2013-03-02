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

class TestHasStatsMixin(TestCase):
    def setUp(self):
        from warlord.stat import HasStats
        class Statable(HasStats):
            pass
        self.statable = Statable()

    def test_add_stat(self):
        self.statable.add_stat('name')
        self.assertTrue(hasattr(self.statable, 'name'))
        self.assertEqual(self.statable.name, 0)
        self.assertTrue(hasattr(self.statable, '_stat_name'))
        self.assertEquals(self.statable._stat_name.value, 0)

    def test_setattr(self):
        self.statable.add_stat('name')
        self.statable.name = 1
        self.assertEquals(self.statable.name, 1)
        self.assertEquals(self.statable._stat_name.value, 1)

    def test_add_max_stat(self):
        self.statable.add_stat('name', max_value=0)
        self.statable.name = 1
        self.assertEquals(self.statable.name, 0)
        self.assertEquals(self.statable.max_name, 0)
        self.assertEquals(self.statable._stat_name.value, 0)

    def test_add_min_stat(self):
        self.statable.add_stat('name', min_value=0)
        self.statable.name = -1
        self.assertEquals(self.statable.name, 0)
        self.assertEquals(self.statable.min_name, 0)
        self.assertEquals(self.statable._stat_name.value, 0)

    def test_add_min_max_stat(self):
        self.statable.add_stat('name', min_value=0, max_value=0)
        self.statable.name = -1
        self.assertEquals(self.statable.name, 0)
        self.assertEquals(self.statable.min_name, 0)
        self.assertEquals(self.statable._stat_name.value, 0)
        self.statable.name = 1
        self.assertEquals(self.statable.name, 0)
        self.assertEquals(self.statable.max_name, 0)
        self.assertEquals(self.statable._stat_name.value, 0)
