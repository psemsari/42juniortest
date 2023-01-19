from dataclasses import dataclass
from typing import List

from player import Player
from bottles import Bottle

@dataclass
class Bot(Player):

    def useBottles(self):
        pass

    def buyInShop(self, itemsList: List[Bottle]):
        pass

    def useWeapon(self, players: List[Player]):
        selectedWeapon = 0
        selectedTarget = 0
        for n, target in enumerate(players):
            if target.hp > players[selectedTarget].hp:
                selectedTarget = n
        self.weapons[selectedWeapon].use(self, players[selectedTarget])
        return
