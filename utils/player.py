from card import Card
from typing import List
import random

class Player:
    
    def __init__(self, name):

        self.name = name
        self.cards:List[Card] = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history:List[Card] = []

    def __str__ (self):
        return f"{self.name} + 'turn count' + {self.turn_count}"

    def play(self):
    #For now I'm putting the count here
        self.turn_count += 1
        myCard = random.choice(self.cards)
        self.history.append(myCard)
        print(self.name + " turn " + self.turn_count + " played: " + myCard.value + myCard.icon )
        return myCard




