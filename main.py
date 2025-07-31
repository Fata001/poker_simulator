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
        player = Hand([deck.deal('HA'), deck.deal('D5')])
        others = [Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')]),
                  Hand([deck.deal('??'), deck.deal('??')])]
        common = Common([deck.deal('D3'), 
                         deck.deal('D2'),
                         deck.deal('D4'), 
                         deck.deal('D0'),
                         deck.deal('S0')])
        
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

    