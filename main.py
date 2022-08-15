import pygame
from pygame.locals import *
import pygame.locals
import crtanje
import os

pygame.init()
screenh = 500
os.system("wmic path Win32_VideoController get CurrentHorizontalResolution > file.txt")
file = open("file.txt", "r")
lista = file.readlines()
broj = lista[2]
broj = broj[1] + broj[3] + broj[5] + broj[7]
screenw = int(broj)
file.close()
os.system("wmic path Win32_VideoController get CurrentVerticalResolution > file.txt")
file = open("file.txt", "r")
lista = file.readlines()
broj = lista[2]
broj = broj[1] + broj[3] + broj[5]
screenh = int(broj)
file.close()
os.system("del /f file.txt")
print(screenh, screenw)

screen = pygame.display.set_mode((screenw-10, screenh-60))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

saved = False
ime = ""
def sejvuj():
    global saved
    global ime
    if saved:
        os.system("del /f "+ime+".png")
        pygame.image.save(screen, ime+".png")
    else:   
        ime = input("Unesite ime: ")
        pygame.image.save(screen, ime+".png")
        saved = True
running = True
screen.fill((255, 255, 255))
flag = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                sejvuj()
            if event.key == pygame.K_0:
                flag = 0
            if event.key == pygame.K_1:
                flag = 1
        if pygame.mouse.get_pressed()[0]:
            if flag == 0:
                crtanje.brush(event.pos[0], event.pos[1], 6, (255, 0, 200), screen)
            elif flag == 1:
                crtanje.rubber(event.pos[0], event.pos[1], 6, screen)
    pygame.display.flip()
    


    
