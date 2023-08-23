from NInARow import Game
from RandomAgent import RA
import numpy as np
import random

class Node():
    def __init__(self,game):
        self.value = 0 
        self.game = game
        self.player = 2
        self.action = None
        self.action_nodes = None

class MCTS():
    def __init__(self,game):
        self.root = Node(game)
    def e_greedy_selection(self,action_nodes,e,maxmin):
        max_nodes = [action_nodes[0]]

        for node in action_nodes:
            if node.value == max_nodes[0].value:
                max_nodes.append(node)
            if maxmin == "max":
                if node.value > max_nodes[0].value:
                    max_nodes = [node]
            elif maxmin == "min":
                if node.value < max_nodes[0].value:
                    max_nodes = [node]

        max_node = max_nodes[random.randint(0,len(max_nodes)-1)]
        if e>random.random():
            max_node = action_nodes[random.randint(0,len(action_nodes)-1)]
        return max_node
    
    def selection(self,e):
        node_to_expand = self.root
        path = [node_to_expand]
        
        while True:
            if node_to_expand.action_nodes != None and node_to_expand.action_nodes !=[]:
                node_to_expand = self.e_greedy_selection(node_to_expand.action_nodes,e,"max")
                path.append(node_to_expand)
            else:
                return path
        
    def expand(self,node_to_expand:Node):
        positions = np.argwhere(node_to_expand.game.board == 0)
        node_to_expand.action_nodes = []

        for pos in positions:
            new_game = Game()
            player = 2 if node_to_expand.player == 1 else 1
            new_game.board = node_to_expand.game.board.copy()
            new_game.board[tuple(pos)] = player
            
            new_node = Node(new_game)
            new_node.action = tuple(pos)
            new_node.player = player
            node_to_expand.action_nodes.append(new_node)
        return node_to_expand

    def backup(self,path,reward):
        for node in path:
            node.value += reward
    
    def rollout(self,node_to_explore:Node):
        players = [RA(1),RA(2)]
        current_p = 1 if node_to_explore.player == 2 else 0
        game = Game()
        game.board = node_to_explore.game.board.copy()
        while True:
            result, player = game.check_outcome()
            if result == "draw":
                return 0
            elif result == "win":
                if player == 2:
                    return -1
                else:
                    return 1
                
            positions = np.argwhere(game.board == 0)
            position_to_play = tuple(players[current_p].pick_action(positions,0))
            possible = game.place_circle(current_p+1,position_to_play)
            if current_p == 0:
                current_p = 1
            else:
                current_p = 0 


game = Game()
mcts = MCTS(game)
for i in range(100000):
    path = mcts.selection(0.2)
    to_explore = mcts.expand(path[-1])
    reward = mcts.rollout(to_explore)
    mcts.backup(path,reward)

class MCTSPLAYER():
    def __init__(self,mcts:MCTS) -> None:
        self.mcts = mcts
        self.current_state = mcts.root
    def update_state(self,new_board):
        if self.current_state.action_nodes != None and self.current_state.action_nodes != []:
            for node in self.current_state.action_nodes:
                if (node.game.board == new_board).all():
                    self.current_state = node
    def pick_action(self,pos,cp):
        if self.current_state.action_nodes == None:
            return pos[random.randint(0,len(pos)-1)]
        if cp == 0:
            max_node = self.mcts.e_greedy_selection(self.current_state.action_nodes,0,"max")
        elif cp == 1:
            max_node = self.mcts.e_greedy_selection(self.current_state.action_nodes,0,"min")
        return max_node.action


win = 0
loss = 0
draw = 0
for i in range(1000):
    mp = MCTSPLAYER(mcts)
    players = [mp,RA(2)]
    game = Game()
    current_player = 0
    #print("GAME________")
    while True:
        #print(game.board)
        result, player = game.check_outcome()
        
        if result == "draw":
            #print(game.board)
            draw+=1
            break
        elif result == "win":
           # print(game.board)
            if player == 2:
                loss+=1
            else:
                win+=1
            break
            

        positions = np.argwhere(game.board == 0)
        #position to play for random or mcts
        
        position_to_play = tuple(players[current_player].pick_action(positions,current_player))
        possible = game.place_circle(current_player+1,position_to_play)
        
        
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0

        for player in players:
            player.update_state(game.board)

print(win)
print(loss)
print(draw)

