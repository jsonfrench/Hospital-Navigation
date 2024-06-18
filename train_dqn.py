import gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import CheckpointCallback
from environment import MedicineEnv

# Create and wrap the environment
env = make_vec_env(MedicineEnv, n_envs=1)

# Define the model
model = DQN('MlpPolicy', env, verbose=1, learning_rate=1e-3, buffer_size=50000, learning_starts=1000, batch_size=32, tau=1.0, gamma=0.99, train_freq=4, target_update_interval=1000, exploration_fraction=0.1, exploration_final_eps=0.02, exploration_initial_eps=1.0, max_grad_norm=10)

# Set up a checkpoint callback to save the model at intervals
checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./models/', name_prefix='dqn_medicine')

# Add debug statements to monitor training progress
print("Starting training...")

# Train the model
model.learn(total_timesteps=10000, callback=checkpoint_callback)

print("Training complete. Saving model...")

# Save the trained model
model.save("dqn_medicine")

print("Model saved. Evaluating...")

# Evaluate the trained model
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward}, Std reward: {std_reward}")

# Load the trained model for visualization
model = DQN.load("dqn_medicine")

# Create the environment
env = MedicineEnv()

# Run a few episodes to visualize the agent's behavior
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
env.close()
