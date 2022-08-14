import pygame
from pygame.locals import *
import pygame.locals

pygame.init()

screenw = 500
screenh = 100

screen = pygame.display.set_mode((screenw, screenh), RESIZABLE)
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

def sejvuj():
    ime = input("Unesite ime")
    pygame.image.save(screen, ime+".png")

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                sejvuj()

    
