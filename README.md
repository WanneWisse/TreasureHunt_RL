# TreasureHunt_RL
Hi everyone! This reposititory will be about my holiday adventure with reinforcement learning. During my Master program I followed multiple agent courses and wanted to know more of the topic of reinforcement learning. 
I am studying the reinforcement learning book of Surton Barton and following the UCL David Silver lectures online.
## Game
To implement the algorithms I have created a very simple game called TreasureHunt. This game is a gridworld game, as in the book, but then with the goal to find a treasure without colliding with the walls! 

## With dynamics
When knowing p(s'|s,a) is knowing the dynamics of the game. So when you take an action a from state s and you know where you will end up. E.g you know the map of the game and so, when you take an action left you know that there is a wall. Having this information you can use this to update the values of the states which you want, this means you can start at these states.

### Value iteration
As algorithms I have implemented value iteration as combination of policy evaluation and iteration.

To find the results you can run treasure_hunt_with_walls or *_without _walls you will get two matrices as output. 
One represents the policy and the other represents the values for every state. 

## Without dymanics 
Now you dont know p(s'|s,a), so you can't directly model v(s) because you dont know what s' will be. But we can estimate v(s) by just trying sequences. easier is to estimate q(s,a) because sequences will exists of S1,A1,R1,S2,A2,R2,..,ST,AT,RT.

### On-policy Monte Carlo
This algorithm works by taking averages of the returns of the sequences from every state action pair(q(s,a)). It is on-policy because the policy where it is learned from is the same as the behaviour policy.

To find the results you can run treasure_hunt_with_walls_without dynamics. As result you will get a list with all the explored states and their corresponding best action, value of the action and how often it is tried.
## Future
In the future I hope to implement Off-policy Monte Carlo and Temporal difference methods.
