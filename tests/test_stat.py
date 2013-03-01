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

class TestStatManager(TestCase):
    def setUp(self):
        from warlord.stat import StatManager
        self.man = StatManager()

    def test_add_stat(self):
        self.man.add_stat('name')
        self.assertEqual(self.man['name'], 0)

    def test_change_stat(self):
        self.man.add_stat('name')
        self.man['name'] = 1
        self.assertEqual(self.man['name'], 1)

    def test_add_min_stat(self):
        self.man.add_stat('name', min_value=0)
        self.assertEqual(self.man['name'], 0)
        self.assertEqual(self.man['min_name'], 0)

    def test_add_min_stat_follows_min(self):
        self.man.add_stat('name', min_value=0)
        self.man['name'] = -1
        self.assertEqual(self.man['name'], 0)

    def test_add_max_stat(self):
        self.man.add_stat('name', max_value=0)
        self.assertEqual(self.man['name'], 0)
        self.assertEqual(self.man['max_name'], 0)

    def test_add_max_stat_follows_max(self):
        self.man.add_stat('name', max_value=0)
        self.man['name'] = 1
        self.assertEqual(self.man['name'], 0)

    def test_add_min_max_stat(self):
        self.man.add_stat('name', min_value=0, max_value=0)
        self.assertEqual(self.man['name'], 0)

    def test_add_min_max_stat_follows_min(self):
        self.man.add_stat('name', min_value=0, max_value=0)
        self.man['name'] = -1
        self.assertEqual(self.man['name'], 0)

    def test_add_min_max_stat_follows_max(self):
        self.man.add_stat('name', min_value=0, max_value=0)
        self.man['name'] = 1
        self.assertEqual(self.man['name'], 0)
