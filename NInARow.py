import numpy as np
class Game():
    def __init__(self):
        self.board = np.zeros((3,3))
        self.N_in_a_row = 3
        self.shape = self.board.shape
    #player1: 1
    #player2: 2
    
    def check_outcome(self):
        players = [1,2]
        #print(players)
        for i in players:
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    if y + self.N_in_a_row-1 < self.shape[1]:
                        if np.all(self.board[x,y:y+self.N_in_a_row] == i):
                            return "win",i
                    if x + self.N_in_a_row-1 < self.shape[0]:
                        if np.all(self.board[x:x+self.N_in_a_row,y] == i):
                            return "win",i
                    if x + self.N_in_a_row-1 < self.shape[0] and y + self.N_in_a_row-1 < self.shape[1]:
                        slice = [self.board[(x+i,y+i)] for i in range(self.N_in_a_row)]
                        if np.all(np.array(slice) == i):
                            return "win",i
        if not np.any(self.board == 0):
            return "draw",i
        return "continue",i
    
    def check_occupied(self,position):
        if self.board[position] != 0:
            return True

    def place_circle(self,player,position):
        if self.check_occupied(position):
            return False
        self.board[position] = player
        return True
        
        

game = Game()
result = game.place_circle(1,(0,0))
print(result)
print(game.check_outcome())
result = game.place_circle(2,(0,1))
print(result)
print(game.check_outcome())
result = game.place_circle(1,(1,0))
print(result)
print(game.check_outcome())
result = game.place_circle(2,(0,2))
print(result)
print(game.check_outcome())
result = game.place_circle(1,(2,0))
print(result)
print(game.check_outcome())
print(game.board)



