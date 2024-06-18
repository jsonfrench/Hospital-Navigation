import gym
from gym import spaces
import numpy as np
import pygame
from dataclasses import dataclass

@dataclass
class Player:
    medicine: int = 0
    delivered: int = 0

class MedicineEnv(gym.Env):
    def __init__(self):
        super(MedicineEnv, self).__init__()
        self.layout = [
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3]
        ]
        self.grid_size = (len(self.layout), len(self.layout[0]))
        self.cell_size = 50
        self.scr_width = self.grid_size[1] * self.cell_size
        self.scr_height = self.grid_size[0] * self.cell_size

        self.action_space = spaces.Discrete(4)  # up, down, left, right
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.grid_size[0], self.grid_size[1], 1), dtype=np.float32)

        self.player = Player()
        self.player_x = 0
        self.player_y = 0
        self.reset()

    def reset(self):
        self.player = Player()
        self.player_x = 0
        self.player_y = 0
        self.layout = [
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3]
        ]
        return self._get_state()

    def step(self, action):
        desired_player_x = self.player_x
        desired_player_y = self.player_y
        if action == 0:  # up
            desired_player_y -= 1
        elif action == 1:  # down
            desired_player_y += 1
        elif action == 2:  # left
            desired_player_x -= 1
        elif action == 3:  # right
            desired_player_x += 1

        if self._is_valid_location((desired_player_x, desired_player_y)):
            self.player_x = desired_player_x
            self.player_y = desired_player_y

        reward = -0.1  # Small penalty for each step
        done = False

        if self.layout[self.player_y][self.player_x] == 2:
            self.layout[self.player_y][self.player_x] = 0
            self.player.medicine += 1
            reward += 1
        elif self.layout[self.player_y][self.player_x] == 3:
            self.player.delivered += self.player.medicine
            self.player.medicine = 0
            reward += 10
            done = True

        return self._get_state(), reward, done, {}

    def _is_valid_location(self, position):
        if not 0 <= position[0] < len(self.layout[0]):
            return False
        if not 0 <= position[1] < len(self.layout):
            return False
        if self.layout[position[1]][position[0]] == 1:
            return False
        return True

    def _get_state(self):
        state = np.zeros(self.grid_size)
        state[self.player_y][self.player_x] = 1  # Mark player position
        for y in range(self.grid_size[0]):
            for x in range(self.grid_size[1]):
                if self.layout[y][x] == 2:
                    state[y][x] = 0.5  # Mark medicine position
                elif self.layout[y][x] == 3:
                    state[y][x] = 0.75  # Mark delivery location
        return state[..., np.newaxis]

    def render(self, mode='human'):
        pygame.init()
        screen = pygame.display.set_mode((self.scr_width, self.scr_height))
        screen.fill("white")
        self._draw_state(screen)
        pygame.display.flip()
        pygame.time.delay(500)

    def _draw_state(self, screen):
        start_x = 0
        for row in self.layout:
            start_y = 0
            for col in row:
                color = "white"
                if col == 1:
                    color = "black"
                elif col == 2:
                    color = "green"
                elif col == 3:
                    color = "purple"
                pygame.draw.rect(screen, color, pygame.Rect(start_y * self.cell_size, start_x * self.cell_size, self.cell_size, self.cell_size))
                start_y += 1
            start_x += 1
        pygame.draw.circle(screen, "red", (self.player_x * self.cell_size + self.cell_size / 2, self.player_y * self.cell_size + self.cell_size / 2), self.cell_size * 0.9 / 2)

    def seed(self, seed=None):
        np.random.seed(seed)

    def close(self):
        pygame.quit()

    def render(self, mode='human'):
        # Pygame rendering code
        if mode == 'human':
            screen.fill("white")
            self.draw_state()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(60)

