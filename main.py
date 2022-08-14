import pygame
from pygame.locals import *

screenw = 500
screenh = 100

screen = pygame.display.set_mode((screenw, screenh), RESIZABLE)
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

def sejvuj():
    ime = input()
    pygame.image.save(screen, ime)

running = True

while running:
    screen.fill((255, 255, 255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()
            exit