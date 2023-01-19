import unittest
from unittest.mock import patch
from dataclasses import dataclass
from player import Player
from weapons import Bazooka, Prout, Sword, Weapon
from bottles import Bottle, Heal, Damage, Force, bottles_list

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.sword = Sword()
        self.bazooka = Bazooka()
        self.prout = Prout()
        self.weapons_list = [self.sword, self.bazooka, self.prout]
        self.heal = Heal()
        self.damage = Damage()
        self.force = Force()
        self.bottles_list = [self.heal, self.damage, self.force]
        self.player1 = Player("John", (self.sword, self.bazooka), 100, 0, [], 1.00, [])
        self.player2 = Player("Mike", (self.prout, self.prout), 100, 0, [], 1.00, [])
    
    def test_announce(self):
        self.player1.announce()
        self.assertEqual(self.player1.name, "John")
        self.assertEqual(self.player1.money, 0)
        self.assertEqual(self.player1.hp, 100)
        
    def test_isAlive(self):
        self.player1.hp = 0
        self.assertFalse(self.player1.isAlive())
        self.player1.hp = 50
        self.assertTrue(self.player1.isAlive())
        
    def test_hasBottles(self):
        self.assertFalse(self.player1.hasBottles())
        self.player1.bottles = [self.heal]
        self.assertTrue(self.player1.hasBottles())
        
    def test_isInventoryFull(self):
        self.player1.bottles = [self.heal, self.damage]
        self.assertTrue(self.player1.isInventoryFull())
        self.player1.bottles = [self.heal]
        self.assertFalse(self.player1.isInventoryFull())
    
    @patch("builtins.input", side_effect=["0", "0", ""])
    def test_useBottles(self, mock_inputs):
        self.player1.hp = 90
        self.player1.bottles = [self.heal]
        self.player1.useBottles([self.player1])
        self.assertEqual(len(self.player1.bottles), 0)

    @patch("builtins.input", side_effect=["0", "", "0", ""])
    def test_buyInShop(self, mock_inputs):
        self.player1.money = 30
        self.player1.buyInShop(bottles_list)
        self.assertEqual(len(self.player1.bottles), 1)
        self.assertEqual(self.player1.money, 20)
        self.player1.money = 0
        self.player1.buyInShop(bottles_list)
        self.assertEqual(len(self.player1.bottles), 1)
        self.assertEqual(self.player1.money, 0)
    
    @patch("builtins.input", return_value="0")
    def test_useWeapon(self, mock_inputs):
        self.player1.useWeapon([self.player2])
        
    def test_endTurn(self):
        self.player1.strengthApplications = [{0: 0.1}]
        self.player1.strength = 1.1
        self.player1.endTurn()
        self.assertEqual(self.player1.strengthApplications, [])
        self.assertEqual(self.player1.strength, 1)

if __name__ == '__main__':
    unittest.main()
