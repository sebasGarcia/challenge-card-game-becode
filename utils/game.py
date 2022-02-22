from player import Player
from typing import List
from player import Deck
from card import Card
class Board:

    def __init__(self):
         self.players:List[Player] = []
         self.turn_count:int = 0
         self.active_cards:List[Card] = []
         self.history_cards:List[Card] = []

    def start_game(self):

        myDeck = Deck()
        myDeck.filldeck()
        myDeck.shuffle()

        player1 = Player("Jessica")
        player2 = Player("Marleen")
        myPlayers = []
        myPlayers.append(player1)
        myPlayers.append(player2)   
        
        myDeck.distribute(myPlayers)
        
#NEXT: Figure out the logic in the game... do history_cards list get filled after each turn, do active cards list only contain cards in the current
#turn? I think the amount of turns depends on the amount of cards that each player has 
        for player in myPlayers:
            #Adding card to the history cards
            self.active_cards()
            self.history_cards(player.play())
            
       


