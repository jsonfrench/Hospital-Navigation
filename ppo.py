from stable_baselines3 import PPO
from environment import MedicineEnv

# Create the custom environment
env = MedicineEnv()

# Initialize the PPO agent
model = PPO('CnnPolicy', env, verbose=1)

# Train the agent
model.learn(total_timesteps=10000)

# Save the model
model.save("ppo_medicine")

# Load the model
model = PPO.load("ppo_medicine")

# Test the trained agent
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

# Close the game
pygame.quit()
