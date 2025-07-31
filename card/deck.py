from random import choice
from card.suit import Suit
from card.kind import Kind
from card.card import Card

# Init Deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in [Suit('C'), Suit('D'), Suit('H'), Suit('S')]:
            for kind in [Kind('A'), Kind('2'), Kind('3'), Kind('4'), Kind('5'), \
                Kind('6'), Kind('7'), Kind('8'), Kind('9'), Kind('0'), Kind('J'), Kind('Q'), Kind('K'),]:
                self.deck.append(Card(suit, kind))
    
    def __str__(self):
        text = ''
        for card in self.deck:
            text += str(card)
        return text
    
    def random_deal(self):
        _temp = choice(self.deck)
        self.deck.remove(_temp)
        return _temp

    def deal(self, card: str):
        if card == '??':
            return Card(Suit('?'), Kind('?'))
        for deck_card in self.deck:
            if str(deck_card) == str(Card(Suit(card[0]), Kind(card[1]))):
                _temp = deck_card
                self.deck.remove(deck_card)
                return _temp
        print('Misdealing. Bye!')
        exit()
