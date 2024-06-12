# Example file showing a basic pygame "game loop"
import pygame

layout = [
     [0,0,0,0,0,0],
     [0,1,0,1,0,0],
     [0,0,0,1,1,0],
     [1,0,0,1,0,0],
     [0,0,0,0,0,0],
     [0,0,1,1,1,1]
]

def draw_grid():
    for i in range(SCR_WIDTH//CELL_SIZE):
            pygame.draw.line(screen, "black", (i*CELL_SIZE,0), (i*CELL_SIZE,SCR_HEIGHT),width=3)
    for i in range(SCR_HEIGHT//CELL_SIZE):
            pygame.draw.line(screen, "black", (0, i*CELL_SIZE), (SCR_WIDTH, i*CELL_SIZE),width=3)

def draw_state():
    start_x = 0
    for row in layout:
        start_y = 0
        for col in row:
            color = "white"
            if(col == 1):
                    color = "black"
            pygame.draw.rect(screen, color, pygame.Rect(start_y*CELL_SIZE, start_x*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            start_y += 1
        start_x += 1

def is_valid_location(position):
     if not 0 <= position[0] < len(layout[0]) :
          return False
     if not 0 <= position[1] < len(layout) :
          return False
     if layout[position[1]][position[0]] == 1:
          return False
     return True

CELL_SIZE = 50
SCR_WIDTH = len(layout[0]) * CELL_SIZE
SCR_HEIGHT = len(layout) * CELL_SIZE

player_x = 0
player_y = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    #Handle input
    desired_player_x = player_x
    desired_player_y = player_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                desired_player_y -= 1
            if event.key == pygame.K_a:
                desired_player_x -= 1
            if event.key == pygame.K_s:
                desired_player_y += 1
            if event.key == pygame.K_d:
                desired_player_x += 1
    if is_valid_location((desired_player_x, desired_player_y)):
         player_x = desired_player_x
         player_y = desired_player_y

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    draw_state()
    draw_grid()

    #Draw player
    pygame.draw.circle(screen, "red", (player_x*CELL_SIZE+CELL_SIZE/2,player_y*CELL_SIZE+CELL_SIZE/2),CELL_SIZE*.9/2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



