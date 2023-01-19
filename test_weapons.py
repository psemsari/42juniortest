import unittest
from weapons import *
from player import Player

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", (Weapon(), Weapon()))
        self.player2 = Player("Mike", (Weapon(), Weapon()))
        self.sword = Sword()
        self.bazooka = Bazooka()
        self.prout = Prout()
        self.weapons_list = [self.sword, self.bazooka, self.prout]
        
    def test_useWeapon(self):
        self.player1.strength = 2
        self.player1.money = 0

        self.sword.use(self.player1, self.player2)
        self.assertEqual(self.player2.hp, 90)
        self.assertEqual(self.player1.money, 3)

        self.bazooka.use(self.player1, self.player2)
        self.assertEqual(self.player2.hp, 70)
        self.assertEqual(self.player1.money, 4)

        self.prout.use(self.player1, self.player2)
        self.assertEqual(self.player2.hp, 68)
        self.assertEqual(self.player1.money, 9)

    def test_str(self):
        self.assertEqual(str(self.sword), "Sword is making 5 dmg and owner gains 3$")
        self.assertEqual(str(self.bazooka), "Bazooka is making 10 dmg and owner gains 1$")


if __name__ == '__main__':
    unittest.main()
