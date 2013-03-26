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

    def test_default_owner(self):
        self.assertTrue(self.item.owner is None)

class TestLimitedUsesMixin(TestCase):
    def setUp(self):
        from warlord.item import Item, LimitedUseMixin
        class LimitedUseItem(LimitedUseMixin, Item):
            pass
        self.item = LimitedUseItem()

    def test_default_uses(self):
        self.assertEqual(self.item.uses, 0)

    def test_use_item_decreases_uses(self):
        self.item.uses = 1
        self.item.use()
        self.assertEquals(self.item.uses, 0)

    def test_use_with_no_uses_raises_error(self):
        from warlord.item import ItemOutOfUsesError
        self.item.uses = 0
        self.assertRaises(ItemOutOfUsesError, self.item.use)

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
        self.item.stats = {'stat': 1}
        self.item.use(unit)
        self.assertEquals(unit.stat, 2)
