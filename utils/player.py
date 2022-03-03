from utils.card import Card
from typing import List
import random


class Player:
    """
    This class represents the player in the game and has the following attributes in the constructor:
    :name: A string which is The name of the player.
    :cards: A list of Card, which are the cards the player has in hand.
    :turn_count: An int that is the amount of times the player has played.
    :number_of_cards: An int representing the number of cards he has left
    :history: A list of Card, which are all the cards he has played
    """

    def __init__(self, name):

        self.name = name
        self.cards: List[Card] = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history: List[Card] = []

    def __str__(self) -> str:
        return f"{self.name} turn count {self.turn_count}"

    def play(self) -> Card:
        """
        Function that will pick a random Card from cards. It will add that card to the history list and will print info about the player and
        the amount of times he has played.
        :return: A Card type that is the card played by the player.
        """
        self.turn_count += 1
        myCard = random.choice(self.cards)
        self.history.append(myCard)
        # Remove card from hand
        self.cards.remove(myCard)
        print(
            "Player "
            + self.name
            + " - turn #"
            + str(self.turn_count)
            + " played card: "
            + str(myCard)
        )
        return myCard


class Deck:
    """
    This class represents the deck in the game, it has the following attributes in the constructor:
    cards: A string w.
    :cards: A list of Card, which contains all the cards in the deck.
    """

    def __init__(self):
        self.cards: List[Card] = []

    def __str__(self) -> str:
        return self.cards

    

    def filldeck(self):
        """  

        This function will use all the possible value options, icons and colors to create a unique deck 
        it will populate the card list of the class
        """

        value_options = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        icon_options = ["♥", " ♦", "♣", "♠"]
        color_options = ["red", "red", "black", "black"]
        for value in value_options:
            for index, icon in enumerate(icon_options):
                card = Card(color_options[index], icon, value)

                self.cards.append(card)


    def shuffle(self):
        
        """  
        This function shuffle the cards inside the list in the class 

        """
        self.cards = random.sample(self.cards, len(self.cards))

    

    def distribute(self, players: list):
        """  
    This function distribute evenly the cards inside the list for all players, the contraint is that the amount of players must be a dividor of 52
    otherwise it will display at message. It has one parameter:
    :param players: A list of objects Player

    """
        cards_per_player = int(len(self.cards) / len(players))

        if len(self.cards) % len(players) == 0:
            cards_distributed = [
                self.cards[i * cards_per_player : (i + 1) * cards_per_player]
                for i in range(
                    (len(self.cards) + cards_per_player - 1) // cards_per_player
                )
            ]

            i = 0
            for player in players:
                if i < len(cards_distributed):
                    player.cards = cards_distributed[i].copy()
                    i += 1

        else:
            print("Sorry, numbers of players can only be a even number or one")

          
            