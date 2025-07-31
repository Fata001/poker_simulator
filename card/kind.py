# Kind of cards
class Kind:
    value = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '0': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 14}

    def __init__(self, kind: str):
        self.kind = kind
        
    def __str__(self):
        return self.kind