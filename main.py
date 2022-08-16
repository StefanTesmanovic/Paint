import pygame
from pygame.locals import *
import pygame.locals
import crtanje
import os

pygame.init()

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

color = (0, 255, 0)

screen = pygame.display.set_mode((screenw-10, screenh-60))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

states = []

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
flag = 0
savingState = False

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
            elif event.key == pygame.K_1:
                flag = 1
            elif event.key == pygame.K_2:
                flag = 2
            elif event.key == pygame.K_3:
                flag = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flag == 2:
                (x, y) = pygame.mouse.get_pos()
                crtanje.floodFill(x, y, screen.get_at((x, y))[:3], color, screen)
            
            if flag <= 1:
                savingState = True
                pikseli = []
                pikseli.append("olovka")
                #imace jedan niz za svaki kvadrat u liniji
            elif flag == 2:
                pikseli = []
                pikseli.append("kofica")
                (x, y) = pygame.mouse.get_pos()
                pikseli.append((x, y, color))
            elif flag == 3:
                (x, y) = pygame.mouse.get_pos()
                color = crtanje.pipeta(x, y, screen)
                flag = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            states.append(pikseli)
            savingState = False
        if pygame.mouse.get_pressed()[0]:
            if flag == 0:
                pikseli.append(crtanje.brush(event.pos[0], event.pos[1], 6, color, screen))
            elif flag == 1:
                pikseli.append(crtanje.rubber(event.pos[0], event.pos[1], 6, screen))
    pygame.display.flip()
    


    
