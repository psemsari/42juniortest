from typing import List


class Weapon:
    name = ""
    damage = 0
    gain = 0

    def __init__(self) -> None:
        pass
    def use(self, player, target):
        target.hp -= self.damage * player.strength
        player.money += self.gain
    def __str__(self) -> str:
        return f"{self.name} is making {self.damage} dmg and owner gains {self.gain}$"

class Sword(Weapon):
    name = "Sword"
    damage = 5
    gain = 3

class Bazooka(Weapon):
    name = "Bazooka"
    damage = 10
    gain = 1

class Prout(Weapon):
    name = "Prout"
    damage = 1
    gain = 5

weapons_list: List[Weapon] = [Sword(), Bazooka(), Prout()]

