from unittest import TestCase
from mock import Mock, patch

class TestCombat(TestCase):
    def test_magical_attack_power(self):
        from warlord.unit import calculate_magical_attack_power
        unitA = Mock()
        unitB = Mock()
        unitA.magic = 0
        unitA.equipped_item.might = 0
        unitA.equipped_item.weapon_counter_bonus.return_value = 0
        unitA.equipped_item.unit_counter_bonus.return_value = 0
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 0)
        unitA.magic = 1
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 1)
        unitA.equipped_item.might = 1
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 2)
        unitA.equipped_item.weapon_counter_bonus.return_value = 1
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 3)
        unitA.equipped_item.unit_counter_bonus.return_value = 1
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 5)
        unitA.equipped_item.might = 2
        self.assertEquals(calculate_magical_attack_power(unitA, unitB), 7)

    def test_physical_attack_power(self):
        from warlord.unit import calculate_physical_attack_power
        unitA = Mock()
        unitB = Mock()
        unitA.strength = 0
        unitA.equipped_item.might = 0
        unitA.equipped_item.weapon_counter_bonus.return_value = 0
        unitA.equipped_item.unit_counter_bonus.return_value = 0
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 0)
        unitA.strength = 1
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 1)
        unitA.equipped_item.might = 1
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 2)
        unitA.equipped_item.weapon_counter_bonus.return_value = 1
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 3)
        unitA.equipped_item.unit_counter_bonus.return_value = 1
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 5)
        unitA.equipped_item.might = 2
        self.assertEquals(calculate_physical_attack_power(unitA, unitB), 7)

    def test_damage_vs_unit(self):
        from warlord.unit import calculate_damage
        unit = Mock()
        unit.strength = 1
        self.assertEquals(calculate_damage(unit, unit), 1)

    def test_damage_vs_unit_with_strength(self):
        from warlord.unit import calculate_damage
        unit = Mock()
        unit.strength = 2
        self.assertEqual(calculate_damage(unit, unit), 2)

    def test_attack_count_vs_unit_with_same_speed(self):
        from warlord.unit import calculate_attack_count
        unit = Mock()
        unit.speed = 1
        self.assertEqual(calculate_attack_count(unit, unit), 1)

    def test_attack_count_vs_unit_with_3_less_speed(self):
        from warlord.unit import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 3
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 1)

    def test_attack_count_vs_unit_with_4_less_speed(self):
        from warlord.unit import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 4
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 2)

    def test_attack_count_vs_unit_with_5_less_speed(self):
        from warlord.unit import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 5
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 2)

    @patch('warlord.unit.calculate_attack_count')
    @patch('warlord.unit.calculate_damage')
    def test_combat(self, calc_atk_cnt, calc_dmg):
        from warlord.unit import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 99
        unitB.health = 99
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 98)
        self.assertEqual(unitB.health, 98)

    @patch('warlord.unit.calculate_attack_count')
    @patch('warlord.unit.calculate_damage')
    def test_combat_with_dead_units_does_nothing(self, calc_atk_cnt, calc_dmg):
        from warlord.unit import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 0
        unitB.health = 0
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 0)
        self.assertEqual(unitB.health, 0)

    @patch('warlord.unit.calculate_attack_count')
    @patch('warlord.unit.calculate_damage')
    def test_combat_where_unit_death_stops_combat(self, calc_atk_cnt, calc_dmg):
        from warlord.unit import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 99
        unitB.health = 1
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 99)
        self.assertEqual(unitB.health, 0)
