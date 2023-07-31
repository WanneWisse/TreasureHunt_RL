import numpy as np


treasure_map = np.array([
                [1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,1],
                [1,1,1,0,1,1,0,1],
                [1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1],])
treasure_pos = (3,2)
treasure_map[treasure_pos] = 2

shape = treasure_map.shape
value_map = np.zeros(shape)
policy = np.zeros(shape).astype("str")
transition_reward=-1

#we expect policy to be argmax
def value_iteration():
    while True:
        max_value_diff = 0
        #for every state
        for row in range(shape[0]):
            for column in range(shape[1]):
                #value of treasure pos and walls should stay 0
                if treasure_map[row,column] == 1 or treasure_map[row,column] == 2:
                    continue

                #check possible actions; up,down,right,left
                possible_actions = []
                #check left of pos
                if treasure_map[row,column-1] != 1:
                    left_pos = row,column-1
                    left_pos_value = value_map[left_pos]
                    possible_actions.append(("left",left_pos_value))
        
                #check right of pos
                if treasure_map[row,column+1] != 1:
                    right_pos = row,column+1
                    right_pos_value = value_map[right_pos]
                    possible_actions.append(("right",right_pos_value))
                #check down of pos
                if treasure_map[row+1,column] != 1:
                    down_pos = row+1,column
                    down_pos_value = value_map[down_pos]
                    possible_actions.append(("down",down_pos_value))
                #check up of pos
                if treasure_map[row-1,column] != 1:
                    up_pos = row-1,column
                    up_pos_value = value_map[up_pos]
                    possible_actions.append(("up",up_pos_value))
                
                resultstate_with_max_value = max(possible_actions,key=lambda item: item[1])
                policy[row,column] = resultstate_with_max_value[0]
                new_value = transition_reward + resultstate_with_max_value[1]
                value_diff = abs(value_map[row,column]-new_value)
                if value_diff>max_value_diff:
                    max_value_diff = value_diff 
                value_map[row,column] = new_value
        
        if max_value_diff < 1:
            return
                
value_iteration()
policy[policy=="0.0"] = "wall"
policy[treasure_pos] = "<3"
print(policy)
print(value_map)



