import gym
from gym import spaces
import numpy as np

class MedicineEnv(gym.Env):
    def __init__(self):
        super(MedicineEnv, self).__init__()
        self.grid_size = (5, 5)
        self.action_space = spaces.Discrete(4)  # Example: up, down, left, right
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.grid_size[0], self.grid_size[1]), dtype=np.float32)
        self.reset()

    def reset(self):
        # Initialize state: player position, medicine position, delivery location
        self.player_pos = [0, 0]
        self.medicine_pos = [2, 2]
        self.delivery_pos = [4, 4]
        self.state = self._get_state()
        return self.state

    def step(self, action):
        # Update player position based on action
        if action == 0:  # up
            self.player_pos[0] = max(self.player_pos[0] - 1, 0)
        elif action == 1:  # down
            self.player_pos[0] = min(self.player_pos[0] + 1, self.grid_size[0] - 1)
        elif action == 2:  # left
            self.player_pos[1] = max(self.player_pos[1] - 1, 0)
        elif action == 3:  # right
            self.player_pos[1] = min(self.player_pos[1] + 1, self.grid_size[1] - 1)

        # Calculate reward
        reward = -0.1  # Small penalty for each step
        if self.player_pos == self.medicine_pos:
            reward += 1  # Reward for picking up medicine
            self.medicine_pos = None  # Remove medicine from grid
        if self.player_pos == self.delivery_pos and self.medicine_pos is None:
            reward += 10  # Reward for delivering medicine
            done = True
        else:
            done = False

        # Get next state
        self.state = self._get_state()
        return self.state, reward, done, {}

    def _get_state(self):
        state = np.zeros(self.grid_size)
        state[tuple(self.player_pos)] = 1  # Mark player position
        if self.medicine_pos:
            state[tuple(self.medicine_pos)] = 2  # Mark medicine position
        state[tuple(self.delivery_pos)] = 3  # Mark delivery location
        return state

    def render(self, mode='human'):
        # Optional: Implement rendering if needed
        pass

env = MedicineEnv()
