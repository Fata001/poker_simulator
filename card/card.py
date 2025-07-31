# The card class
class Card:
    def __init__(self, suit, kind):
        self.suit = suit
        self.kind = kind

    def __str__(self):
        return str(self.suit) + str(self.kind)