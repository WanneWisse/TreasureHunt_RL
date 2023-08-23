import numpy as np
class Game():
    def __init__(self):
        self.board = np.zeros((4,4))
        self.shape = self.board.shape
    #player1: 1
    #player2: 2
    
    def check_outcome(self):
        players = [1,2]
        for player in players:
            if player == 1:
                print(player)
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    if y + 3 < self.shape[1]:
                        if np.all(self.board[x,y:y+4] == player):
                            return "win",player
                    if x + 3 < self.shape[0]:
                        if np.all(self.board[x:x+4,y] == player):
                            return "win",player
                    if x + 3 < self.shape[0] and y + 3 < self.shape[1]:
                        slice = [self.board[(x+i,y+i)] for i in range(4)]
                        if np.all(np.array(slice) == player):
                            return "win",player
            if not np.any(self.board == 0):
                return "draw",player
            return "continue",player
    
    def check_occupied(self,position):
        if self.board[position] != 0:
            return True

    def place_circle(self,player,position):
        if self.check_occupied(position):
            return False
        self.board[position] = player
        return True
        
        

# game = Game()
# result = game.place_circle(1,(0,0))
# print(result)
# result = game.place_circle(2,(0,1))
# print(result)
# result = game.place_circle(1,(1,0))
# print(result)
# result = game.place_circle(2,(0,2))
# print(result)
# result = game.place_circle(1,(2,0))
# print(result)
# result = game.place_circle(2,(0,3))
# print(result)
# result = game.place_circle(1,(3,0))
# print(result)
# print(game.board)



