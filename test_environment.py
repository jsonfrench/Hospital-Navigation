import environment
import numpy as np

env = environment.MedicineEnv()

state = env.reset()
done = False
total_reward = 0

while not done:
    action = env.action_space.sample()  # take a random action
    next_state, reward, done, info = env.step(action)
    total_reward += reward
    env.render()

print(f"Total Reward: {total_reward}")
