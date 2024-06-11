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

def draw_squares():
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

CELL_SIZE = 50
SCR_WIDTH = len(layout[0]) * CELL_SIZE
SCR_HEIGHT = len(layout) * CELL_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    
    draw_squares()
    draw_grid()

    #pygame.draw.rect(screen,"black", pygame.Rect(100,100,10,10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



