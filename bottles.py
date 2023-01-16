from typing import List
import math

class Bottle:
    name: str = ""
    price: int = 0

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return self.name

    def use(self, player, target) -> bool:
        raise NotImplemented()

class Heal(Bottle):
    name = "Heal"
    price = 10

    def use(self, player, target: None) -> bool:
        player.hp = min(100, player.hp + 10)


class Damage(Bottle):
    name = "Damage"
    price = 3

    def use(self, player, target) -> bool:
        target.hp -= math.ceil(25 * player.strength)
        return True

class Force(Bottle):
    name = "Force"
    price = 5

    def use(self, player, target) -> bool:
        if any([app > 0 for _, app in player.strengthApplications.items()]):
            return False
        player.strength += 0.10
        player.strengthApplications.append({3: 0.10})
        return True

bottles_list: List[Bottle] = [Heal(), Damage(), Force()]
