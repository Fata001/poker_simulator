from card.deck import Deck
from game.hand import Hand
from game.common import Common
from game.table import Table
from game.simulation import Simulation

if __name__ == '__main__':
    
    print('>>> GAME STARTED')
    
    N = 5000
    win, lose, split = 0, 0, 0
    
    for i in range(N):
        deck = Deck()
        
        """ '[suit][kind]' 
        suit --> C, D, H, S
        kind --> 2,3,4,5,6,7,8,9,0,J,Q,K,A
        '??' --> complete() will deal random cards from the deck
        """
        player = Hand([deck.deal('H7'), deck.deal('H8')])
        others = [Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')])]
        common = Common([deck.deal('H0'), 
                         deck.deal('S9'),
                         deck.deal('S0'), 
                         deck.deal('D4'),
                         deck.deal('DA')])
        
        table = Table()
        table.deal(deck, common, player, others)
        
        simulation = Simulation(table)
        simulation.complete()
        
        result = simulation.simulation()
        if result == True:
            win += 1
        elif result == False:
            lose += 1
        else:
            split += 1
    
    # Print result
    print('Win:\t', round(win/N*100, 2), '%')
    print('Lose:\t', round(lose/N*100, 2), '%')
    print('Split:\t', round(split/N*100, 2), '%')
    print()

    