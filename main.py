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

state = []

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
###################################

def empty(list):
    if len(list) == 0:
        return True
    return False

def undo():
    global state
    pass
            
running = True
screen.fill((255, 255, 255))
flag = 1
pikseli = []
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
            if event.key == pygame.K_2:
                flag = 2
            if event.key == pygame.K_3:
                flag = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flag <= 1:
                pikseli = []
                pikseli.append("cetkica")
            if flag == 2:
                (x,y) = pygame.mouse.get_pos()
                crtanje.tekst(x, y, screen)
            if flag == 3:
                start = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            state.append(pikseli)
            if flag == 3:
                end = pygame.mouse.get_pos()
                crtanje.crtanjeLinija(start, end, (100, 100, 100), state, screen)

        if pygame.mouse.get_pressed()[0]:
            if flag == 0:
                pikseli.append(crtanje.brush(event.pos[0], event.pos[1], 6, (255, 0, 200), screen))
            elif flag == 1:
                pikseli.append(crtanje.rubber(event.pos[0], event.pos[1], 6, screen))
    pygame.display.flip()
