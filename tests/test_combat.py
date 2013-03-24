from unittest import TestCase
from mock import Mock, patch

class TestCombat(TestCase):
    def test_magical_attack_power(self):
        from warlord.combat import calculate_magical_attack_power
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
        from warlord.combat import calculate_physical_attack_power
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

    @patch('warlord.combat.calculate_magical_attack_power')
    def test_attack_power_with_magical_item(self, calc_mag_atk_pwr):
        from warlord.combat import calculate_attack_power
        unitA = Mock()
        unitB = Mock()
        unitA.equipped_item.type = 'magical'
        calculate_attack_power(unitA, unitB)
        calc_mag_atk_pwr.assert_called_once_with(unitA, unitB)

    @patch('warlord.combat.calculate_physical_attack_power')
    def test_attack_power_with_physical_item(self, calc_phys_atk_pwr):
        from warlord.combat import calculate_attack_power
        unitA = Mock()
        unitB = Mock()
        unitA.equipped_item.type = 'physical'
        calculate_attack_power(unitA, unitB)
        calc_phys_atk_pwr.assert_called_once_with(unitA, unitB)

    @patch('warlord.combat.calculate_physical_attack_power')
    def test_physical_damage(self, calc_phys_atk_pwr):
        from warlord.combat import calculate_physical_damage
        unitA = Mock()
        unitB = Mock()
        unitB.defense = 0
        calc_phys_atk_pwr.return_value = 0
        self.assertEquals(calculate_physical_damage(unitA, unitB), 0)
        calc_phys_atk_pwr.return_value = 1
        self.assertEquals(calculate_physical_damage(unitA, unitB), 1)
        unitB.defense = 1
        self.assertEquals(calculate_physical_damage(unitA, unitB), 0)

    @patch('warlord.combat.calculate_physical_attack_power')
    def test_physical_damage_is_never_negative(self, calc_phys_atk_pwr):
        from warlord.combat import calculate_physical_damage
        unitA = Mock()
        unitB = Mock()
        unitB.defense = 1
        calc_phys_atk_pwr.return_value = 0
        self.assertEquals(calculate_physical_damage(unitA, unitB), 0)

    @patch('warlord.combat.calculate_magical_attack_power')
    def test_magical_damage(self, calc_mag_atk_pwr):
        from warlord.combat import calculate_magical_damage
        unitA = Mock()
        unitB = Mock()
        unitB.resistance = 0
        calc_mag_atk_pwr.return_value = 0
        self.assertEquals(calculate_magical_damage(unitA, unitB), 0)
        calc_mag_atk_pwr.return_value = 1
        self.assertEquals(calculate_magical_damage(unitA, unitB), 1)
        unitB.resistance = 1
        self.assertEquals(calculate_magical_damage(unitA, unitB), 0)

    @patch('warlord.combat.calculate_magical_attack_power')
    def test_magical_damage_is_never_negative(self, calc_mag_atk_pwr):
        from warlord.combat import calculate_magical_damage
        unitA = Mock()
        unitB = Mock()
        unitB.resistance = 1
        calc_mag_atk_pwr.return_value = 0
        self.assertEquals(calculate_magical_damage(unitA, unitB), 0)

    @patch('warlord.combat.calculate_magical_damage')
    def test_damage_with_magical_item(self, calc_mag_dmg):
        from warlord.combat import calculate_damage
        unitA = Mock()
        unitB = Mock()
        unitA.equipped_item.type = 'magical'
        calculate_damage(unitA, unitB)
        calc_mag_dmg.assert_called_once_with(unitA, unitB)

    @patch('warlord.combat.calculate_physical_damage')
    def test_damage_with_physical_item(self, calc_phys_dmg):
        from warlord.combat import calculate_damage
        unitA = Mock()
        unitB = Mock()
        unitA.equipped_item.type = 'physical'
        calculate_damage(unitA, unitB)
        calc_phys_dmg.assert_called_once_with(unitA, unitB)

    def test_attack_count_vs_unit_with_same_speed(self):
        from warlord.combat import calculate_attack_count
        unit = Mock()
        unit.speed = 1
        self.assertEqual(calculate_attack_count(unit, unit), 1)

    def test_attack_count_vs_unit_with_3_less_speed(self):
        from warlord.combat import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 3
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 1)

    def test_attack_count_vs_unit_with_4_less_speed(self):
        from warlord.combat import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 4
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 2)

    def test_attack_count_vs_unit_with_5_less_speed(self):
        from warlord.combat import calculate_attack_count
        unitA = Mock()
        unitB = Mock()
        unitA.speed = 5
        unitB.speed = 0
        self.assertEqual(calculate_attack_count(unitA, unitB), 2)

    def test_combat_raises_out_of_range_when_not_in_range(self):
        from warlord.combat import UnitOutOfRangeError, combat
        unitA = Mock()
        unitB = Mock()
        weapon = Mock()
        weapon.attack_range = [0]
        unitA.equipped_item = weapon
        tileA = Mock()
        tileA.location = (0, 0)
        tileA.unit = unitA
        unitA.tile = tileA
        tileB = Mock()
        tileB.location = (0, 2)
        tileB.unit = unitB
        unitB.tile = tileB
        self.assertRaises(UnitOutOfRangeError, combat, unitA, unitB)

    @patch('warlord.combat.calculate_attack_count')
    @patch('warlord.combat.calculate_damage')
    @patch('warlord.combat.is_in_range')
    def test_combat(self, calc_atk_cnt, calc_dmg, in_rng):
        from warlord.combat import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 99
        unitB.health = 99
        unitA.equipped_item.uses = 99
        unitB.equipped_item.uses = 99
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        in_rng.return_value = True
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 98)
        self.assertEqual(unitB.health, 98)

    @patch('warlord.combat.calculate_attack_count')
    @patch('warlord.combat.calculate_damage')
    @patch('warlord.combat.is_in_range')
    def test_combat_with_dead_units_does_nothing(self, calc_atk_cnt, calc_dmg, in_rng):
        from warlord.combat import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 0
        unitB.health = 0
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        in_rng.return_value = True
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 0)
        self.assertEqual(unitB.health, 0)

    @patch('warlord.combat.calculate_attack_count')
    @patch('warlord.combat.calculate_damage')
    @patch('warlord.combat.is_in_range')
    def test_combat_where_unit_death_stops_combat(self, calc_atk_cnt,
            calc_dmg, in_rng):
        from warlord.combat import combat
        unitA = Mock()
        unitB = Mock()
        unitA.health = 99
        unitB.health = 1
        unitA.equipped_item.uses = 99
        unitB.equipped_item.uses = 99
        calc_atk_cnt.return_value = 1
        calc_dmg.return_value = 1
        in_rng.return_value = True
        combat(unitA, unitB)
        self.assertEqual(unitA.health, 99)
        self.assertEqual(unitB.health, 0)

    @patch('warlord.combat.do_combat_round')
    def test_combat_loop_changes_attack_count_when_out_of_uses(self,
            do_cmbt_rnd):
        from warlord.combat import do_combat_loop
        unitA = Mock()
        unitB = Mock()
        unitA.equipped_item.uses = 1
        atk_cnts = [99, 0]
        def side_effect(*args, **kwargs):
            unitA.equipped_item.uses -= 1
        do_cmbt_rnd.side_effect = side_effect
        do_combat_loop([unitA, unitB], atk_cnts)
        self.assertEquals(do_cmbt_rnd.call_count, 1)
        self.assertEquals(atk_cnts, [0, 0])
