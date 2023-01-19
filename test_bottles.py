import unittest
from bottles import Bottle, Heal, Damage, Force
from weapons import Weapon
from player import Player

class TestBottle(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", (Weapon(), Weapon()))
        self.player2 = Player("Mike", (Weapon(), Weapon()))
        self.heal = Heal()
        self.damage = Damage()
        self.force = Force()
        self.bottles_list = [self.heal, self.damage, self.force]
    
    def test_Heal(self):
        self.player1.hp = 90
        self.heal.use(self.player1, None)
        self.assertEqual(self.player1.hp, 100)
        
    def test_Damage(self):
        self.player1.hp = 100
        self.player1.strength = 2
        self.damage.use(self.player1, self.player2)
        self.assertEqual(self.player2.hp, 50)
        
    def test_Force(self):
        self.player1.strength = 1
        self.player1.strengthApplications = []
        self.force.use(self.player1, None)
        self.assertEqual(self.player1.strength, 1.1)
        self.assertEqual(self.player1.strengthApplications, [{3: 0.1}])
        self.force.use(self.player1, None)
        self.assertEqual(self.player1.strengthApplications, [{3: 0.1}])

if __name__ == '__main__':
    unittest.main()
