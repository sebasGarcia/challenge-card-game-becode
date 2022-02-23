from utils.player import Player
from typing import List
from utils.player import Deck
from card import Card

"""
    This class represents the Board in the game and has the following attributes in the constructor:
    :players: A list of the class Player with the players that will participate in the game.
    :turn_count: Int number that represents the specific turn, it increments after every turn .
    :active cards: a List of the class Card, that contains the last card played by each player.
    :history_cards: A list of Card, which contains all the cards played by the players
    """


class Board:
    def __init__(self):
        self.players: List[Player] = []
        self.turn_count: int = 0
        self.active_cards: List[Card] = []
        self.history_cards: List[Card] = []

    def __str__(self) -> str:
        return f"Players: {self.players} - Turns: {self.turn_count} - Active cards: {self.active_cards} - History cards: {self.history_cards}"

    """
    This method starts the game with 2 players:
    First a deck object will be created and the methods filldeck() and shuffle() will be called
    Two player objects will be created 
    The distribute method from Deck will be called to distribute the cards among the players
    Total turns will depend on the amount of cards each player has, in this case 26, so 26 turns
    A user plays one card per turn and that card is added to the active_cards and history_cards
    The active cards only shows the cards used in that particular turn
    The amount of history cards is shown at the end
    After all cards have been used the game stopts
    """

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

        total_turns = len(myPlayers[0].cards)

        i = 0
        while i < total_turns:
            self.turn_count = i + 1
            
            print(
                "-----------------Turn #" + str(self.turn_count) + "------------------"
            )

            for player in myPlayers:

                current_card = player.play()
                self.active_cards.append(current_card)
                self.history_cards.append(current_card)

            print(
                "The number of cards in history is now: " + str(len(self.history_cards))
            )

            if len(self.history_cards) < 52:
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