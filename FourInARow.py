import numpy as np
class FourInARow():
    def __init__(self):
        self.board = np.zeros((6,6))
        self.shape = self.board.shape
        self.player = 1
    #player1: 1
    #player2: 2
    def check_outcome(self,):
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if y + 3 < self.shape[1]:
                    if np.all(self.board[x,y:y+4] == self.player):
                        return "win",self.player
                if x + 3 < self.shape[0]:
                    if np.all(self.board[x:x+4,y] == self.player):
                        return "win",self.player
                if x + 3 < self.shape[0] and y + 3 < self.shape[1]:
                    slice = [self.board[(x+i,y+i)] for i in range(4)]
                    if np.all(np.array(slice) == self.player):
                        return "win",self.player
        if not np.any(self.board == 0):
            return "draw",self.player
        return "continue",self.player
    
    def check_occupied(self,position):
        if self.board[position] != 0:
            return True

    def change_player(self):
        if self.player == 1:
            self.player+=1
        else:
            self.player-=1

    def place_circle(self,position):
        if self.check_occupied(position):
            return "not possible",self.player
        self.board[position] = self.player
        outcome = self.check_outcome()
        self.change_player()
        return outcome
        
        

game = FourInARow()
result = game.place_circle((0,0))
print(result)
result = game.place_circle((0,1))
print(result)
result = game.place_circle((1,0))
print(result)
result = game.place_circle((0,2))
print(result)
result = game.place_circle((2,0))
print(result)
result = game.place_circle((0,3))
print(result)
result = game.place_circle((3,0))
print(result)
print(game.board)



