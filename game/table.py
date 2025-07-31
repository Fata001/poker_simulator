class Table:
    def deal(self, deck, common, player, others: list):
        self.deck = deck
        self.common = common
        self.player = player
        self.others = others
        
    def show_table(self):
        print('TABLE:')
        print('Deck:', self.deck)
        print('Common cards:', self.common)
        print("Players's hand:", self.player)
        print("Other's hand:")
        for i, hand in enumerate(self.others):
            print(str(i+2) + '.player:', str(hand))
        print()