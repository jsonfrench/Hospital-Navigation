import gym
from stable_baselines3 import DQN
from environment import MedicineEnv
import time

# Load the trained model
model = DQN.load("dqn_medicine")

# Create the environment
env = MedicineEnv()

# Run a few episodes to visualize the agent's behavior
obs = env.reset()
for episode in range(5):  # Run 5 episodes for visualization
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        time.sleep(0.1)  # Add a small delay to slow down the rendering

env.close()
