import unittest

from project.hero import Hero


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.superman = Hero('Gosho', 20, 40, 25)
        self.batman = Hero('Pesho', 20, 40, 25)

    def test_init(self):
        self.assertEqual(self.superman.username, 'Gosho')
        self.assertEqual(self.superman.health, 40)
        self.assertEqual(self.superman.level, 20)
        self.assertEqual(self.superman.damage, 25)

    def test_battle(self):
        with self.assertRaises(Exception) as ex:
            self.batman.username = 'Gosho'
            self.superman.battle(self.batman)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

        self.batman.username = 'Pesho'

        with self.assertRaises(ValueError) as ex:
            self.superman.health = 0
            self.superman.battle(self.batman)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.superman.health = 40

        with self.assertRaises(ValueError) as ex:
            self.batman.health = 0
            self.superman.battle(self.batman)

        self.assertEqual(f"You cannot fight Pesho. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        self.assertEqual(self.superman.battle(self.batman), 'Draw')

    def test_battle_win(self):
        self.batman.damage = 1
        battle = self.superman.battle(self.batman)
        self.assertEqual(self.superman.level, 21)
        self.assertEqual(self.superman.health, 25)
        self.assertEqual(self.superman.damage, 30)
        self.assertEqual(battle, "You win")

    def test_battle_lose(self):
        self.superman.damage = 1
        battle = self.superman.battle(self.batman)
        self.assertEqual(self.batman.level, 21)
        self.assertEqual(self.batman.health, 25)
        self.assertEqual(self.batman.damage, 30)
        self.assertEqual(battle, "You lose")


    def test_str(self):
        self.assertEqual(str(self.superman), f"Hero Gosho: 20 lvl\nHealth: 40\nDamage: 25\n")


if __name__ == '__main__':
    unittest.main()