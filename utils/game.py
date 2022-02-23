from utils.player import Player
from typing import List
from utils.player import Deck
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
        
      
        #That number of turns is equal to the number of cards each player has in their hands..
        total_turns = len(myPlayers[0].cards)

        i=0
        while (i < total_turns):
            self.turn_count  = i+1
            print("-----------------Turn #" + str(self.turn_count)+ "------------------") 

        #    print("Turn count#" + str(turn)) 
            for player in myPlayers:

               # print("Player: "+ player.name + ""str(turn)) 
                #Adding card to the history cards
                current_card = player.play()
                self.active_cards.append(current_card)
                self.history_cards.append(current_card)
            
            print("The number of cards in history is now: " + str(len(self.history_cards)))
            
            
            if(len(self.history_cards)<52):
                print("Active cards:")
                
                for card in self.active_cards:
                    print(str(card))
                
                if len(self.active_cards) > 0:
                    self.active_cards.clear()
            else:
                print("Game's over, thank you for playing!")
           
            i+=1            
       

myBoard = Board()
myBoard.start_game()

