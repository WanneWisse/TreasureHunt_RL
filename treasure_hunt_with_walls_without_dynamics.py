from typing_extensions import override
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
        self.action_space = ["left","right","up","down"]
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
        reward = -1
        done = False
        #check if hit wall
        if self.states[result_state] == 1:
            reward = -10
            done = True
        elif self.states[result_state] == 2:
            reward = 100
            done = True
        self.player_state = result_state
        return result_state,reward,done

class Learning_Algorithm():
    def __init__(self,game:Game) -> None:
        self.game = game
        self.action_space = game.action_space
        self.state_action_values = {}
        self.policy = []
    def pick_action(self,state):
        max_action = random.randint(0,3)
        if state in self.state_action_values and 0.2<random.random():
            action_values = self.state_action_values[state]
            max_action = np.argmax(action_values)
        return max_action
    def show_policy(self):
        pass

class Q_learning(Learning_Algorithm):
    def __init__(self, game:Game) -> None:
        super().__init__(game)
        self.gamma = 1
        self.lr = 1

    def draw_step(self):
        current_state = self.game.player_state
        action_index = self.pick_action(current_state)
        result_state,reward,done = self.game.take_action(self.action_space[action_index])
        return current_state, action_index, result_state,reward,done 
        

    def step_to_value(self,current_state, action, result_state,reward):

        if current_state not in self.state_action_values:
            self.state_action_values[current_state] = np.zeros(len(self.action_space))
        if result_state not in self.state_action_values:
            self.state_action_values[result_state] = np.zeros(len(self.action_space))   
        
        old_value_of_cs = self.state_action_values[current_state][action]
        
        
        value_of_result_state = max(self.state_action_values[result_state])
            
        new_value_of_cs = old_value_of_cs + self.lr * (reward + self.gamma * value_of_result_state - old_value_of_cs)
        self.state_action_values[current_state][action] = new_value_of_cs

    @override
    def show_policy(self):
        state_action_values = list(self.state_action_values.items())
        for state,action_values in state_action_values:
            action_index = np.argmax(action_values)
            action_value = action_values[action_index]
            self.policy.append((state,action_value,action_index))
        print(self.policy)
    

class MonteCarlo(Learning_Algorithm):
    def __init__(self,game:Game):
        super().__init__(game)
    def draw_episode(self):
        sequence = []
        current_state = self.game.player_state
        while True:
            action_index = self.pick_action(current_state)
            result_state,reward,done = self.game.take_action(self.action_space[action_index])
            sequence.append([current_state,action_index,reward])
            current_state = result_state
            if done:
                break
        return sequence
    def episode_to_values(self,sequence):
        G = 0
        episode = sequence[::-1]
        for time_step in episode:
            state = time_step[0]
            action_index = time_step[1]
            reward = time_step[2]
            G = 1*G + reward
            if state not in self.state_action_values:
                self.state_action_values[state] = np.empty(len(self.action_space), dtype=object)
                self.state_action_values[state].fill((0,1))
            old_mean,count = self.state_action_values[state][action_index]
            self.state_action_values[state][action_index] = (old_mean + (G-old_mean)/count,count+1)
    
    @override
    def show_policy(self):
        state_action_values = list(self.state_action_values.items())
        for state,value_amount_tried in state_action_values:
            max_index = 0
            max_value = value_amount_tried[0][0]
            for index, (value, amount_tried) in enumerate(value_amount_tried):
                if value > max_value:
                    max_index = index
                    max_value = value
            self.policy.append([state,max_index,max_value])
        print(self.policy)
                

#Treasure at coor 1,4
game = Game((1,4))

#montecarlo algorithm
mc = MonteCarlo(game)
#30000 episodes
for i in range(30000):
    #one episode in world
    sequence = mc.draw_episode()
    #update values using all SAR of episode using G
    mc.episode_to_values(sequence)
    #after one episode wall or terminal 
    game.player_state = game.get_start_state()
#show final policy
mc.show_policy()

#qlearning algorithm
q = Q_learning(game)
#1000 episodes
for i in range(1000):
    #one step in world
    current_state, action_index, result_state,reward,done = q.draw_step()
    #update value using SARS
    q.step_to_value(current_state,action_index,result_state,reward)
    #stop if wall or terminal
    if done:
        game.player_state = game.get_start_state()
#show final policy
q.show_policy()
