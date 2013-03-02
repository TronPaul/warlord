from unittest import TestCase
from mock import Mock

class TestUnit(TestCase):
    def setUp(self):
        from warlord.unit import Unit
        self.unit = Unit()

    def test_default_team(self):
        self.assertEqual(self.unit.team, 0)

    def test_default_tile(self):
        self.assertTrue(self.unit.tile is None)

    def test_default_health(self):
        self.assertEquals(self.unit.health, 0)

    def test_default_max_health(self):
        self.assertEquals(self.unit.max_health, 0)

    def test_default_strength(self):
        self.assertEquals(self.unit.strength, 0)

    def test_default_speed(self):
        self.assertEquals(self.unit.speed, 0)

    def test_default_luck(self):
        self.assertEquals(self.unit.luck, 0)

    def test_default_skill(self):
        self.assertEquals(self.unit.skill, 0)

    def test_default_defense(self):
        self.assertEquals(self.unit.defense, 0)

    def test_evade(self):
        self.unit.speed = 1
        self.assertEquals(self.unit.evade, 2)
        self.unit.luck = 1
        self.assertEquals(self.unit.evade, 3)
        self.unit.speed = 2
        self.assertEquals(self.unit.evade, 5)

    def test_health_does_not_go_below_0(self):
        self.unit.health -= 1
        self.assertEquals(self.unit.health, 0)

    def test_health_does_not_go_above_max_health(self):
        self.unit.health += 1
        self.assertEquals(self.unit.health, 0)

    def test_default_inventory(self):
        self.assertEqual(self.unit.inventory, [])

    def test_default_equipped_item(self):
        self.assertEqual(self.unit.equipped_item, None)

    def test_add_item(self):
        item = Mock()
        self.unit.add_item(item)
        self.assertEqual(len(self.unit.inventory), 1)
        self.assertEqual(self.unit.inventory[0], item)

    def test_remove_item(self):
        item = Mock()
        self.unit.inventory.append(item)
        self.unit.remove_item(item)
        self.assertEqual(len(self.unit.inventory), 0)

    def test_equip_item(self):
        item = Mock()
        self.unit.inventory.append(item)
        self.unit.equip_item(item)
        self.assertEqual(self.unit.equipped_item, item)

    def test_equip_item_item_not_in_inventory(self):
        from warlord.unit import ItemNotInInventoryError
        item = Mock()
        self.assertRaises(ItemNotInInventoryError, self.unit.equip_item, item)

    def test_is_passible(self):
        tile = Mock()
        self.assertTrue(self.unit.is_passible(tile))

    def test_is_passible_without_tile(self):
        self.assertTrue(not self.unit.is_passible(None))

    def test_is_visible_raises_not_implemented(self):
        tile = Mock()
        self.assertRaises(NotImplementedError, self.unit.is_visible, tile)

    def test_default_experience(self):
        self.assertEquals(self.unit.experience, 0)

    def test_default_level(self):
        self.assertEquals(self.unit.level, 1)

    def test_add_experience(self):
        self.unit.add_experience(1)
        self.assertEquals(self.unit.experience, 1)

    def test_add_experience_with_level_up_levels_up(self):
        self.unit.add_experience(100)
        self.assertEquals(self.unit.experience, 0)
        self.assertEquals(self.unit.level, 2)

    def test_add_experience_with_level_2_levels_up_to_3(self):
        self.unit.level = 2
        self.unit.add_experience(100)
        self.assertEquals(self.unit.level, 3)
    def test_add_experience_with_level_up_and_extra_levels_up_with_extra_exp(self):
        self.unit.add_experience(101)
        self.assertEquals(self.unit.experience, 1)
        self.assertEquals(self.unit.level, 2)

    def test_add_experience_with_level_up_calls_level_up_stats(self):
        mock = Mock()
        self.unit.level_up_stats = mock
        self.unit.add_experience(100)
        mock.assert_called_once_with()

    def test_add_experience_with_multi_level_up_calls_level_up_stats(self):
        mock = Mock()
        self.unit.level_up_stats = mock
        self.unit.add_experience(200)
        mock.assert_called_with()
        self.assertEquals(mock.call_count, 2)
