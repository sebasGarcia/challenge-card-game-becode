from card import Card
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
        self.cards:List[Card] = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history:List[Card] = []

    def __str__ (self) -> str:
        return f"{self.name} turn count {self.turn_count}"

    def play(self) -> Card:
        """
        Function that will pick a random Card from cards. It will  add that card to the history list and will print info about the player and
        the amount of times he has played.
        :return: A Card type that is the card played by the player.
        """
        self.turn_count += 1
        myCard = random.choice(self.cards)
        self.history.append(myCard)
        print(self.name + " turn " + self.turn_count + " played: " + myCard.value + myCard.icon )
        return myCard

class Deck: 
   
    def __init__(self):
        self.cards:List[Card] = []



    def filldeck(self):

        value_options = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        icon_options = ['♥',' ♦', '♣', '♠']
        color_options =["red", "red", "black", "black"]
        for value in value_options:
            for index, icon in enumerate(icon_options):
                card = Card(color_options[index],icon,value)
                #print(card)
                self.cards.append(card)


    def shuffle(self):
        self.cards = random.sample(self.cards,len(self.cards))
        #print("len cards: "+ str(len(self.cards)))
       # print("------Inside shuffle-------")
       # print(self.cards)
        #print("Len: " +str(len(random.sample(self.cards,len(self.cards)))))
        #print("--------------------------")
    
    def distribute(self,players:list):
        cards_per_player=int(len(self.cards)/len(players))
        #print(cards_per_player)
        if(len(self.cards)%len(players)==0):
            cards_distributed = [self.cards[i * cards_per_player:(i + 1) * cards_per_player] for i in range((len(self.cards) + cards_per_player - 1) // cards_per_player) ]
           # print("------------Cards distributed----------------")
            #print(cards_distributed)
            #print("----------------------------")


            i = 0
            for player in players:
                if(i<len(cards_distributed)):
                    player.cards.append(cards_distributed[i])
                    i+=1

        else:
            print("Sorry, numbers of players can only be a even number or one")



player1 = Player("Jessica")
player2 = Player("Marleen")
player3 = Player("Carlos")
player4 = Player("Maritza")
myPlayers = []
myPlayers.append(player1)
myPlayers.append(player2)
myPlayers.append(player3)
myPlayers.append(player4)
print(player1)
print(player2)
print(player3)
print(player4)

myDeck = Deck()

myDeck.filldeck()
myDeck.shuffle()
myDeck.distribute(myPlayers)


print("-----p1----------------------------------------")
for card in player1.cards:
    print(str(card))
print("-----p2----------------------------------------")
for card in player2.cards:
    print(str(card))
print("-----p3----------------------------------------")
for card in player3.cards:
    print(str(card))
print("-----p4----------------------------------------")
for card in player4.cards:
    print(str(card))
