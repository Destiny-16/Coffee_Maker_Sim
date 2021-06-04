import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init() #sound effects init

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30 #frames per second
LIGHT_BLUE = (0, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coffee Maker")
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(FPS) #keep loop running at right speed
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill(LIGHT_BLUE)


    #flip always last
    pygame.display.flip()

pygame.quit()
