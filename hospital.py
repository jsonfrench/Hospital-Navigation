#Boilerplate code gotten from https://www.pygame.org/docs/
import pygame
from dataclasses import dataclass

#Struct that holds player data (amount of medicine)
@dataclass
class Player:
     medicine: int = 0
     delivered: int = 0

#Defines map of tiles
#1 = wall
#2 = medicine
#3 = delivery point
layout = [
     [0,2,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,1,0,1,1,1],
     [0,0,0,0,1,0,1,0,0,2,0],
     [0,0,0,0,1,0,1,0,0,0,0],
     [0,0,0,0,2,0,0,0,0,0,0],
     [0,1,1,1,0,0,0,1,1,1,0],
     [0,1,0,0,0,0,1,1,0,0,0],
     [0,1,0,0,0,0,1,1,0,0,0],
     [0,1,0,0,1,0,0,0,0,0,3]
]

#----------Functions----------#

#Draws a grid on the screen
def draw_grid():
    for i in range(SCR_WIDTH//CELL_SIZE):
            pygame.draw.line(screen, "black", (i*CELL_SIZE,0), (i*CELL_SIZE,SCR_HEIGHT),width=3)
    for i in range(SCR_HEIGHT//CELL_SIZE):
            pygame.draw.line(screen, "black", (0, i*CELL_SIZE), (SCR_WIDTH, i*CELL_SIZE),width=3)

#Fills in the color of each tile
def draw_state():
    start_x = 0
    for row in layout:
        start_y = 0
        for col in row:
            color = "white"
            if(col == 1):
                    color = "black"
            elif(col == 2):
                    color = "green"
            elif(col == 3):
                    color = "purple"
            pygame.draw.rect(screen, color, pygame.Rect(start_y*CELL_SIZE, start_x*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            start_y += 1
        start_x += 1
        draw_player()

#Draws player onto the board
def draw_player():
    pygame.draw.circle(screen, "red", (player_x*CELL_SIZE+CELL_SIZE/2,player_y*CELL_SIZE+CELL_SIZE/2),CELL_SIZE*.9/2)

#Returns a list of tuples containing the coordinates of every tile of specified type
def get_tile(type):
    wall_locations = []
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            if layout[row][col] == type:
                wall_locations.append((col, row))
    return wall_locations

#Returns locations of tiles, players, and amount of medicine
def get_state():
    state=[]
    for x in range(1,4):
        state.append(get_tile(x))
    state.append((player_x,player_y))
    state.append(player.medicine)
    state.append(player.delivered)
    return(state)

#Collision detection
def is_valid_location(position):
     if not 0 <= position[0] < len(layout[0]):
          return False
     if not 0 <= position[1] < len(layout):
          return False
     if layout[position[1]][position[0]] == 1:
          return False
     return True

#----------Constants----------#
CELL_SIZE = 50
SCR_WIDTH = len(layout[0]) * CELL_SIZE
SCR_HEIGHT = len(layout) * CELL_SIZE

player_x = 0
player_y = 0

player = Player()

#Pygame setup (more boilerplate)
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
clock = pygame.time.Clock()
running = True

#----------Game loop----------#

while running:

    #Handle input
    desired_player_x = player_x
    desired_player_y = player_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #pygame.QUIT event means the user clicked X to close your window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #move up
                desired_player_y -= 1
            if event.key == pygame.K_a: #move left
                desired_player_x -= 1
            if event.key == pygame.K_s: #move down
                desired_player_y += 1
            if event.key == pygame.K_d: #move right
                desired_player_x += 1
            if event.key == pygame.K_SPACE: #pickup/dropoff medicine
                if layout[player_y][player_x] == 2:
                    layout[player_y][player_x] = 0
                    player.medicine += 1
                elif layout[player_y][player_x] == 3:
                    player.delivered += player.medicine
                    player.medicine = 0
                    print("Delivered medicine!")
                print("Medicine:", player.medicine)
            if event.key == pygame.K_e: #get state (debuggine)
                print(get_state())
        if event.type == pygame.MOUSEBUTTONDOWN:    #Click a square to build a wall 
            mouse_x, mouse_y = event.pos            #Click a wall to knock it down
            mouse_x //= CELL_SIZE
            mouse_y //= CELL_SIZE
            layout[mouse_y][mouse_x] = 1 if layout[mouse_y][mouse_x] == 0 else 0

    if is_valid_location((desired_player_x, desired_player_y)):
         player_x = desired_player_x
         player_y = desired_player_y

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    draw_state()
    draw_grid()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



