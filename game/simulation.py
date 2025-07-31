from utils.evaluation import evaluation_hand
class Simulation:
    def __init__(self, table):
        self.table = table
    
    def complete(self):
        """Fill missing cards"""
        for i, card in enumerate(self.table.common.cards):
            if str(card) == '??':
                self.table.common.cards[i] = self.table.deck.random_deal()
        
        for i, card in enumerate(self.table.player.cards):
            if str(card) == '??':
                self.table.player.cards[i] = self.table.deck.random_deal()
        
        for i, hand in enumerate(self.table.others):
            for k, card in enumerate(hand.cards):
                if str(card) == '??':
                    self.table.others[i].cards[k] = self.table.deck.random_deal()
        
    def compare(self, value: list):
        min_length = min(len(value[0]), len(value[1]))
        for i in range(min_length):
            if value[0][i] > value[1][i]:
                return True
            elif value[0][i] < value[1][i]:
                return False
        return None
                
        
    
    def simulation(self):
        self.complete()
        
        player_value = evaluation_hand(
            self.table.common.cards[:] + self.table.player.cards[:])
        
        others_value = []
        for i, opponent in enumerate(self.table.others):
            others_value.append(evaluation_hand(
                self.table.common.cards[:] + opponent.cards[:]))
    
        vectors = []
        for hand in [player_value] + others_value:
            vector = [hand['rank'], hand['kind']]
            for x in hand['kicker']:
                vector.append(x)
            vectors.append(vector)
        
        hand_values = []
        for opponent in vectors[1:]:
            hand_values.append(self.compare([vectors[0], opponent]))
        
        if False in hand_values:
            return False
        elif None in hand_values:
            return None
        else:
            return True