class Hand:
    def __init__(self, cards: list):
        self.cards = cards

    def __str__(self):
        text = ''
        for card in self.cards:
            text += str(card) + ' '
        return text