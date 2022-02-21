class Symbol:

    icon_options = ['♥',' ♦', '♣', '♠']

    def __init__(self, color, icon):

        self.color = color
        self.icon = icon

    def __str__ (self):
        return f"{self.color} - {self.icon}"

class Card(Symbol):

    value_options = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, color, icon, value):
        Symbol.__init__(self, color, icon)
        self.value = value
    
    def __str__ (self):
        return f"{self.color} - {self.icon} - {self.value}"


myCard = Card("red",'♥', '10')
print(myCard)