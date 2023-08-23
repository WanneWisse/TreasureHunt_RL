import numpy as np
import random

class RA():
    def __init__(self,player) -> None:
        self.player = player
    def pick_action(self,pos,current_player):
        return pos[random.randint(0,len(pos)-1)]
    def update_state(self,pos):
        pass
    
    
        

