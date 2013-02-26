from unittest import TestCase
from mock import Mock

class TestUnit(TestCase):
    def setUp(self):
        from warlord.unit import Unit
        self.unit = Unit()

    def test_default_location(self):
        self.assertEqual(self.unit.location, (0, 0))

    def test_default_health(self):
        self.assertEquals(self.unit.health, 0)

    def test_default_strength(self):
        self.assertEquals(self.unit.strength, 0)

    def test_damage_vs_unit(self):
        from warlord.unit import calculate_damage
        self.unit.strength = 1
        self.assertEqual(calculate_damage(self.unit, self.unit), 1)

    def test_damage_vs_unit_with_strength(self):
        from warlord.unit import calculate_damage
        self.unit.strength = 2
        self.assertEqual(calculate_damage(self.unit, self.unit), 2)

    def test_default_speed(self):
        self.assertEquals(self.unit.speed, 0)

    def test_attack_count_vs_unit(self):
        from warlord.unit import calculate_attack_count
        self.assertEqual(calculate_attack_count(self.unit, self.unit), 1)

    def test_attack_count_vs_other_unit(self):
        from warlord.unit import Unit, calculate_attack_count
        unitOther = Unit()
        self.unit.speed = 1
        self.assertEqual(calculate_attack_count(self.unit, unitOther), 2)

    def test_combat(self):
        from warlord.unit import Unit, combat
        unitOther = Unit()
        unitOther.health = 99
        self.unit.health = 99
        self.unit.strength = 1
        unitOther.strength = 1
        combat(self.unit, unitOther)
        self.assertEqual(self.unit.health, 98)
        self.assertEqual(unitOther.health, 98)

    def test_combat_with_dead_units_does_nothing(self):
        from warlord.unit import Unit, combat
        unitOther = Unit()
        self.unit.strength = 1
        unitOther.strength = 1
        combat(self.unit, unitOther)
        self.assertEqual(self.unit.health, 0)
        self.assertEqual(unitOther.health, 0)

    def test_combat_where_unit_death_stops_combat(self):
        from warlord.unit import Unit, combat
        unitOther = Unit()
        self.unit.strength = 1
        unitOther.strength = 1
        unitOther.health = 1
        self.unit.health = 99
        combat(self.unit, unitOther)
        self.assertEqual(self.unit.health, 99)
        self.assertEqual(unitOther.health, 0)

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

    def test_is_passible_with_impassible_tile(self):
        tile = Mock()
        tile.impassible.return_value = True
        self.assertTrue(not self.unit.is_passible(tile))
