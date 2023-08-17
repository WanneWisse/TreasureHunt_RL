import numpy as np
import random
from FourInARow import Game

class RA():
    def __init__(self,player) -> None:
        self.player = player
    def pick_action(self,game:Game):
        positions = np.argwhere(game.board == 0)
        return positions[random.randint(0,len(positions)-1)]
    
    
        

