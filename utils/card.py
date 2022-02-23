import sys
#Since there was a problem importing the files in the folder utils I included sys and used sys.path.append to append the location of folder
sys.path.append('C:/Users/sebas/Desktop/BeCode/Projects/challenge-card-game-becode/utils')

class Symbol:

    icon_options = ['♥',' ♦', '♣', '♠']

    def __init__(self, color, icon):

        self.color = color
        self.icon = icon

    def __str__ (self) -> str:
        return f"{self.color} - {self.icon}"

class Card(Symbol):

    value_options = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, color, icon, value):
        Symbol.__init__(self, color, icon)
        self.value = value
    
    def __str__ (self) -> str:
        return f"{self.color} - {self.icon} - {self.value}"
    
    def __repr__(self) -> str:
        return f"{self.color} - {self.icon} - {self.value}"
