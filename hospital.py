# Example file showing a basic pygame "game loop"
import pygame


SCR_WIDTH = 800
SCR_HEIGHT = SCR_WIDTH

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
    num_lines = 10
    
    for i in range(num_lines):
            pygame.draw.line(screen, "black",(i*SCR_WIDTH/num_lines,0),(i*SCR_WIDTH/num_lines,SCR_HEIGHT),width=3)
            pygame.draw.line(screen, "black",(0,i*SCR_HEIGHT/num_lines),(SCR_WIDTH, i*SCR_HEIGHT/num_lines) ,width=3)

    pygame.draw.line(screen, "black",(0,0),(SCR_WIDTH,SCR_HEIGHT),width=3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()