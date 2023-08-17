from FourInARow import Game
from RandomAgent import RA
import numpy as np
import random

    
game = Game()

class Node():
    def __init__(self,game):
        self.value = game.board
        self.action_nodes = None

class MCTS():
    def __init__(self):
        self.root = Node(game)
        self.player = 1
        self.depth = 1
    def e_greedy_selection(self,action_nodes,e):
        max_node = action_nodes[0]
        for node in action_nodes:
            if node.value > max_node:
                max_node = node
        if e>random.random():
            max_node = action_nodes[random.randint(0,len(action_nodes)-1)]
        return max_node
    def selection(self):
        while True:
            node_to_expand = self.root
            if node_to_expand != None:
                node_to_expand = self.e_greedy_selection(self.root.action_nodes)
            else:
                


                
        positions = np.argwhere(game.board == 0)
        pass
    def backup():
        pass
    def rollout(player1,player2):
        ra1 = RA(1)
        results = []
        players = [ra1,ra2]
        start_player = 0
        for i in range(10):
            game = Game()
            current_player = start_player
            while True:
                position = tuple(players[current_player].pick_action(game))
                result,player = game.place_circle(players[current_player].player,position)

                if result == "draw" or result == "win":
                    results.append((player,result))
                    print(game.board)
                    break
                
                if current_player == 0:
                    current_player = 1
                else:
                    current_player = 0    

            if start_player == 0:
                start_player=1
            else:
                start_player=0
        print(results)
    def explansion():
        pass


# ra1 = RA(1)
# ra2 = RA(2)

# results = []
# players = [ra1,ra2]
# start_player = 0
# for i in range(10):
#     game = Game()
#     current_player = start_player
#     while True:
#         position = tuple(players[current_player].pick_action(game))
#         result,player = game.place_circle(players[current_player].player,position)

#         if result == "draw" or result == "win":
#             results.append((player,result))
#             print(game.board)
#             break
        
#         if current_player == 0:
#             current_player = 1
#         else:
#             current_player = 0    

#     if start_player == 0:
#         start_player=1
#     else:
#         start_player=0
# print(results)