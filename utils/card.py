import sys

# Since there was a problem importing the files in the folder utils I included sys and used sys.path.append to append the location of my folder
sys.path.append(
    "C:/Users/sebas/Desktop/BeCode/Projects/challenge-card-game-becode/utils"
)

"""
    This class represents the Symbol of every card which is composed by an icon and a color, the class has attributes:
    :color: a string attribute.
    :icon: one of following options: '♥',' ♦', '♣', '♠'.

    """


class Symbol:

    icon_options = ["♥", " ♦", "♣", "♠"]

    def __init__(self, color, icon):

        self.color = color
        self.icon = icon

    def __str__(self) -> str:
        return f"{self.color} - {self.icon}"


"""
    This class represents the card, it inherits from the class Symbol and adds a value to it.
    The class has attributes:
    :color: a string attribute.
    :icon: one of following options: '♥',' ♦', '♣', '♠'.
    Color and icon are inherited from Symbol
    :value which is one of the following 'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'

    """


class Card(Symbol):

    value_options = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, color, icon, value):
        Symbol.__init__(self, color, icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.color} - {self.icon} - {self.value}"

    def __repr__(self) -> str:
        return f"{self.color} - {self.icon} - {self.value}"
