'''
Created on Sep 6, 2018
@author: Angelo Zhu
This game is not an original idea. 
'''

import game_mechanics
import game_visual

def get_board_size():
    return int(input('Choose a board size: '))

if __name__ == '__main__':  
    game = game_mechanics.Game(get_board_size())
    game_visual.run(game)