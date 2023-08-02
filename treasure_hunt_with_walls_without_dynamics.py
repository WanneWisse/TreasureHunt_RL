import numpy as np
import random

class Game():
    def __init__(self,treasure_pos) -> None:
        self.states = np.array([
                        [1,1,1,1,1,1,1,1],
                        [1,3,0,0,0,0,0,1],
                        [1,1,1,0,1,1,0,1],
                        [1,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1],])
        self.states[treasure_pos] = 2
        self.player_state = self.get_start_state()
    def get_start_state(self):
        start_states = np.where(self.states==3)
        start_state = (start_states[0][0],start_states[1][0])
        return start_state
    def map_action_state(self,action):
        if action == "left":
            new_state = [self.player_state[0],self.player_state[1]-1]
        if action == "right":
            new_state = [self.player_state[0],self.player_state[1]+1]
        if action == "up":
            new_state = [self.player_state[0]-1,self.player_state[1]]
        if action == "down":
            new_state = [self.player_state[0]+1,self.player_state[1]]
        return new_state
        

    def take_action(self,action):
        result_state = tuple(self.map_action_state(action))
        reward = 0
        done = False
        #check if hit wall
        if self.states[result_state] == 1:
            self.player_state = self.get_start_state()
            reward = -10
            done = True
        elif self.states[result_state] == 2:
            self.player_state = self.get_start_state()
            reward = 100
            done = True
        else:
            self.player_state = result_state
        
        return result_state,reward,done
    

class MonteCarlo():
    def __init__(self,game:Game):
        self.game = game
        self.state_action_values = {}
    def draw_episode(self):
        sequence = []
        current_state = str(self.game.player_state)
        while True:
            action = self.pick_action(current_state)
            result_state,reward,done = self.game.take_action(action)
            sequence.append([current_state,action,reward])
            current_state = result_state
            if done:
                break
        return sequence
    def episode_to_values(self,sequence):
        actions = ["left","right","up","down"]
        G = 0
        episode = sequence[::-1]
        for time_step in episode:
            state = str(time_step[0])
            action = time_step[1]
            reward = time_step[2]
            G = 1*G + reward
            if state in self.state_action_values:
                if action in self.state_action_values[state]:
                    old_mean,count = self.state_action_values[state][action]
                    self.state_action_values[state][action] = (old_mean + (G-old_mean)/count,count+1)
                else:
                    self.state_action_values[state][action] = (G,1)
            else:
                self.state_action_values[state] = {}
                for action in actions:
                    self.state_action_values[state][action] = (0,1)
                self.state_action_values[state][action] = (G,1)
   
    def pick_action(self,state):
        actions = ["left","right","up","down"]
        if state in self.state_action_values:
            action_values = list(self.state_action_values[state].items())
            max_action = action_values[0][0]
            max_value = action_values[0][1]
            for action, value in action_values:
                if value > max_value:
                    max_action = action
                    max_value = value
            if 0.01> random.random():
                max_action = actions[random.randint(0,3)]
        else:
            max_action = actions[random.randint(0,3)]
        return max_action
        
#initialize game with treasure position                
game = Game((3,2))
#create montecarlo alogrithm
mc = MonteCarlo(game)
#run for 300000 iterations
#TODO: check if q_values have changed with certain amount otherwise stop instead of iterations
for i in range(300000):
    sequence = mc.draw_episode()
    mc.episode_to_values(sequence)

#get policy after iterations
state_action_values = list(mc.state_action_values.items())
policy = []
for state,action_values in state_action_values:
    action_values = list(action_values.items())
    max_action = action_values[0][0]
    max_value = action_values[0][1]
    for action, value in action_values:
        if value > max_value:
            max_action = action
            max_value = value
    policy.append([state,max_action,max_value])
print("policy after iterations:")
print(policy)
