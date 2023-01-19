from player import Player
from bot import Bot
from typing import Dict, List, Tuple
from bottles import Bottle, bottles_list
from weapons import Bazooka, Prout, Sword, Weapon

def selectPlayerPlayingFirst(players: List[Player], nRound: int) -> List[Player]:
    firstPlayer = nRound % len(players)
    playersRound = players[firstPlayer:] + players[:firstPlayer]
    return playersRound

def playRound(players: List[Player], nRound: int):
    print(f"Round {nRound:d}")
    playersRound = selectPlayerPlayingFirst(players, nRound)
    for player in playersRound:
        player.announce()
        # Utilisation des fioles
        player.useBottles(playersRound)
        # Achat boutique
        player.buyInShop(bottles_list)
        # Utilise son arme
        player.useWeapon(playersRound)
        player.endTurn()

def main():
    nPlayer = 0
    nBot = 0
    while (nPlayer + nBot < 2 or nPlayer + nBot > 10):
        print("Minimum 2 players/bots and Maximum 10 players/bots")
        nPlayer = int(input("number of players > "))
        nBot = int(input("number of bots > "))

    players = []
    for number in range(nPlayer):
        name = input(f"Name for player {number} >")
        players.append(Player(name, (Sword(), Prout()), money = 10))

    for number in range(nBot):
        players.append(Bot(f"Bot{number}", (Sword(), Prout()), money = 10))

    nRound = 0
    while all([player.isAlive() for player in players]):
        playRound(players, nRound)
        nRound += 1

if __name__ == "__main__":
    main()
