from card.kind import Kind

class Simulation:
    def __init__(self, table):
        self.table = table
    
    def complete(self):
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



    def value(self, card: str):
        return Kind.value[card[1]]
    
    
    def evaluation(self, cards):
        
        value_from_seven = {'rank': 0, 'kind': 0, 'kicker': [], '_set': []}
        seven_cards = set()
        for card in cards:
            seven_cards.add(str(card))
        
        # Royal Flush
        for suit in ['C', 'D', 'H', 'S']:
            _set = set()
            for kind in ['A', '0', 'J', 'Q', 'K']:
                _set.add(suit + kind)
            if _set.issubset(seven_cards):
                value_from_seven['rank'] = 9
                value_from_seven['_set'] = _set
                return value_from_seven
        
        # Straight Flush ***!!!
        for suit in ['C', 'D', 'H', 'S']:
            _set = []
            for kind in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']:
                if (suit + kind) in seven_cards:
                    _set.append(suit + kind)
                elif len(_set) < 5:
                    _set = []
                if len(_set) > 4:
                    _set = _set[-5:]  
                    value_from_seven['rank'] = 8
                    value_from_seven['kind'] = self.value(_set[-1])
                    value_from_seven['_set'] = _set
                    return value_from_seven
        
        # Kind counter
        k_counter = {}
        for card in seven_cards:
            if card[1] in k_counter.keys():
                k_counter[card[1]] += 1
            else:
                k_counter[card[1]] = 1
        
        # Four of a Kind
        for kind in k_counter.items():
            if kind[1] == 4:
                _set = []
                for card in seven_cards:
                    if card[1] == kind[0]:
                        _set.append(card)
                value_from_seven['rank'] = 7
                value_from_seven['kind'] = self.value(_set[0])
                value_from_seven['kicker'] = [self.value(sorted(seven_cards.difference(_set), key=self.value)[-1])]
                value_from_seven['_set'] = _set
                return value_from_seven
        
        # Full house
        value = 0
        for kind in k_counter.items():
            if kind[1] == 3:
                if Kind.value[kind[0]] > value:
                    value = Kind.value[kind[0]]
                    _set = []
                    for card in seven_cards:
                        if card[1] == kind[0]:
                            _set.append(card)
                    value_from_seven['rank'] = 3
                    value_from_seven['kind'] = self.value(_set[0])*3
                    value_from_seven['kicker'] = [self.value(sorted(seven_cards.difference(_set), key=self.value)[-1]), self.value(sorted(seven_cards.difference(_set), key=self.value)[-2])]
                    value_from_seven['_set'] = _set
        
        if value_from_seven['rank'] == 3:
            _value_from_seven = value_from_seven['kind']
            k_counter2 = k_counter.copy()
            k_counter2.pop(_set[0][1])
            value = 0
            for kind in k_counter2.items():
                if kind[1] == 3 or kind[1] == 2:
                    if Kind.value[kind[0]] > value:
                        value = Kind.value[kind[0]]
                        _set2 = []
                        for card in seven_cards:
                            if card[1] == kind[0]:
                                _set2.append(card)
                        _set2 = _set2[:2]
                        value_from_seven['rank'] = 6
                        value_from_seven['kind'] = self.value(_set[0])*2 + _value_from_seven
                        value_from_seven['kicker'] = []
                        value_from_seven['_set'] = _set + _set2
        
        if value_from_seven['rank'] == 6:
            return value_from_seven
                   
        # Suit counter
        s_counter = {}
        for card in seven_cards:
            if card[0] in s_counter.keys():
                s_counter[card[0]] += 1
            else: s_counter[card[0]] = 1
            
        # Flush
        for suit in s_counter.items():
            if suit[1] > 4:
                _set = []
                for card in seven_cards:
                    if card[0] == suit[0]:
                            _set.append(card)
                _set = sorted(_set, key=self.value)[-5:]
                value_from_seven['rank'] = 5
                value_from_seven['kind'] = self.value(_set[-1])
                value_from_seven['kicker'] = []
                value_from_seven['_set'] = _set
                return value_from_seven
        
        # Straight
        _set = []
        for kind in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']:
            for card in seven_cards:
                if kind == card[1]:
                    _set.append(card)
                    break
            if _set:
                if _set[-1][1] != kind and len(_set) < 5:
                    _set = []
                elif _set[-1][1] != kind and len(_set) > 4:
                    break
        
        if len(_set) > 4:
            _set = _set[-5:]
            value_from_seven['rank'] = 4
            value_from_seven['kind'] = self.value(_set[-1])
            value_from_seven['kicker'] = []
            value_from_seven['_set'] = _set
            return value_from_seven
        
        # Drill (three of a kind)
        if value_from_seven['rank'] == 3:
            return value_from_seven
        
        # Two pair
        value = 0
        for kind in k_counter.items():
            if kind[1] == 2:
                if Kind.value[kind[0]] > value:
                    value = Kind.value[kind[0]]
                    _set = []
                    for card in seven_cards:
                        if card[1] == kind[0]:
                            _set.append(card)
                    value_from_seven['rank'] = 1
                    value_from_seven['kind'] = self.value(_set[0])
                    value_from_seven['kicker'] = [self.value(sorted(seven_cards.difference(_set), key=self.value)[-1]), self.value(sorted(seven_cards.difference(_set), key=self.value)[-2]), self.value(sorted(seven_cards.difference(_set), key=self.value)[-3])]
                    value_from_seven['_set'] = _set
        
        if value_from_seven['rank'] == 1:
            _value_from_seven = value_from_seven['kind']
            k_counter2 = k_counter.copy()
            k_counter2.pop(_set[0][1])
            value = 0
            for kind in k_counter2.items():
                if kind[1] == 3 or kind[1] == 2:
                    if Kind.value[kind[0]] > value:
                        value = Kind.value[kind[0]]
                        _set2 = []
                        for card in seven_cards:
                            if card[1] == kind[0]:
                                _set2.append(card)
                        _set2 = _set2[:2]
                        value_from_seven['rank'] = 2
                        value_from_seven['kind'] = self.value(_set2[0]) + _value_from_seven
                        value_from_seven['kicker'] = [self.value(sorted(seven_cards.difference(_set), key=self.value)[-1])]
                        value_from_seven['_set'] = _set + _set2
                        
        if value_from_seven['rank'] == 2:
            return value_from_seven
        
        # One pair
        if value_from_seven['rank'] == 1:
            return value_from_seven
        
        # High card
        value_from_seven['rank'] = 0
        value_from_seven['kind'] = self.value(sorted(seven_cards, key=self.value)[-1])
        value_from_seven['kicker'] = [self.value(sorted(seven_cards, key=self.value)[-i]) for i in range(2, 7)]
        value_from_seven['_set'] = [sorted(seven_cards, key=self.value)[-1]]
        
        return value_from_seven
        
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
        
        player_value = self.evaluation(
            self.table.common.cards[:] + self.table.player.cards[:])
        
        others_value = []
        for i, opponent in enumerate(self.table.others):
            others_value.append(self.evaluation(
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