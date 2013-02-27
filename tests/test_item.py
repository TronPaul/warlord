from unittest import TestCase
from mock import Mock

class TestItem(TestCase):
    def setUp(self):
        from warlord.item import Item
        self.item = Item()

    def test_default_value(self):
        self.assertEqual(self.item.value, 0)

    def test_default_name(self):
        self.assertEqual(self.item.name, '')

class TestLimitedUsesMixin(TestCase):
    def setUp(self):
        from warlord.item import Item, LimitedUsesMixin
        class LimitedUseItem(LimitedUsesMixin, Item):
            pass
        self.item = LimitedUseItem()

    def test_default_uses(self):
        self.assertEqual(self.item.uses, 0)

    def test_use_item_decreases_uses(self):
        self.item.uses = 1
        self.item.use()
        self.assertEquals(self.item.uses, 0)

class TestStatChangingMixin(TestCase):
    def setUp(self):
        from warlord.item import Item, StatChangingMixin
        class StatChangingItem(StatChangingMixin, Item):
            pass
        self.item = StatChangingItem()

    def test_default_stats(self):
        self.assertEquals(self.item.stats, {})

    def test_use_item_affects_stats(self):
        unit = Mock()
        unit.stat = 1
        self.item.uses = 1
        self.item.stats = {'stat': 1}
        self.item.use(unit)
        self.assertEquals(unit.stat, 2)
