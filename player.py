import dataclasses
from typing import Dict, List, Tuple
from bottles import Bottle, bottles_list
from weapons import Weapon

@dataclasses.dataclass
class Player:
    name: str
    weapons: Tuple[Weapon, Weapon]
    hp: int = 100
    money: int = 0
    bottles: List[Bottle] = dataclasses.field(default_factory=list)
    strength: float = 1.00
    strengthApplications: List[Dict[int, float]] = dataclasses.field(default_factory=list) 

    def announce(self):
        print(f"{self.name}'s turn with {self.money}$ and {self.hp}/100 HP:")

    def isAlive(self) -> bool:
        return self.hp > 0

    def endTurn(self):
        newApplications = []
        for applications in self.strengthApplications:
            remainingRounds = list(applications.keys())[0]
            gainToRemove = list(applications.values())[0]

            if remainingRounds <= 0:
                self.strength -= gainToRemove
            else:
                newApplications.append({remainingRounds - 1: gainToRemove})

        self.strengthApplications = newApplications

    def hasBottles(self) -> bool:
        return len(self.bottles) > 0
    def isInventoryFull(self) -> bool:
        return len(self.bottles) >= 2

    # Utilisation des fioles
    def useBottles(self, players):
        if self.hasBottles():
            selectedBottle = "1"
            while selectedBottle.strip():
                print("You can use:\n{:s}".format('\n'.join([str(index) + ". " + str(bottle) for (index, bottle) in enumerate(self.bottles) if bottle])))
                selectedBottle = input("Select a bottle or press enter > ")
                try:
                    nSelectedBottle = int(selectedBottle.strip())
                except Exception:
                    nSelectedBottle = None
                if nSelectedBottle != None:
                    bottle = self.bottles[nSelectedBottle]
                    if not bottle:
                        continue
                    bottle = self.bottles.pop(nSelectedBottle)
                    print("You can use on :")
                    for n, target in enumerate(players):
                        print(f"{n} - {target.name} with {target.hp}hp")
                    selectedTarget = int(input("selecte one target > "))
                    if not bottle.use(self, players[selectedTarget]):
                        print("You failed to use your bottle...")
                        self.bottles.append(bottle)

    # Achat boutique
    def buyInShop(self, itemsList: List[Bottle]):
        if not self.isInventoryFull() and self.money > 0 and len(itemsList) > 0:
            selectedBottle = "1"
            while selectedBottle.strip() and not self.isInventoryFull() and self.money > 0 and len(itemsList) > 0:
                print("You can buy but you have {:d}$:\n{:s}".format(self.money, '\n'.join([f"{index:d}. {str(bottle)} - {bottle.price}$" for (index, bottle) in enumerate(itemsList)])))
                selectedBottle = input("Select a bottle or press enter > ")
                try:
                    nSelectedBottle = int(selectedBottle.strip())
                except Exception:
                    nSelectedBottle = None
                if nSelectedBottle != None:
                    bottle = itemsList[nSelectedBottle]
                    self.bottles.append(bottle)
                    self.money -= bottle.price

    # Utilise son arme
    def useWeapon(self, players):
        selectedWeapon = "1"
        while selectedWeapon.strip():
            print("You can use:\n{:s}".format('\n'.join([f"{index:d}. {str(weapon)}" for (index, weapon) in enumerate(self.weapons)])))
            selectedBottle = input("Select a weapon > ")
            try:
                nSelectedWeapon = int(selectedBottle.strip())
            except Exception:
                nSelectedWeapon = None
            if nSelectedWeapon != None:
                print("You can attack :")
                for n, target in enumerate(players):
                    print(f"{n} - {target.name} with {target.hp}hp")
                selectedTarget = int(input("selecte one target > "))
                self.weapons[nSelectedWeapon].use(self, players[selectedTarget])
                return

