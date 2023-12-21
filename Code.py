import gym
import time
import random
from IPython.display import clear_output
import numpy as np

env = gym.make("FrozenLake-v1")


state = env.reset()
done = False
actions = {"w": 3, "s": 1, "a": 0, "d": 2}

while True:        
    clear_output(wait=True)
    env.render()
    time.sleep(0.5)
    action = actions[input('choose an action: w(Up), s(Down), a(Left), d(Right)')]
    new_state, reward, done, info = env.step(action)
  
    if done:
      
        clear_output(wait=True)
        env.render()
      
        if reward == 1:
            print("Congrates, You reached the goal!")
          
        else:
            print("Ops, You fell through a hole!")
            clear_output(wait=True)
        break
    state = new_state


env.close()
