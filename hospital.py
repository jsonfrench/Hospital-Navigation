# Example file showing a basic pygame "game loop"
import pygame



layout = [
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]
]

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
    
    #Create grid
    for i in range(SCR_WIDTH//CELL_SIZE):
            pygame.draw.line(screen, "black", (i*CELL_SIZE,0), (i*CELL_SIZE,SCR_HEIGHT),width=3)
    for i in range(SCR_HEIGHT//CELL_SIZE):
            pygame.draw.line(screen, "black", (0, i*CELL_SIZE), (SCR_WIDTH, i*CELL_SIZE),width=3)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



