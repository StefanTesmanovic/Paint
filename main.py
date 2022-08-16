from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from operator import ne, truediv
import pygame, sys

screenw = 500
screenh = 500
lista_stanja = []
stack_za_redo = []

screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Paint")


running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()



def empty(list):
    if len(list) == 0:
        return True
    return False

def undo():
    n = len(lista_stanja) - 1
    
    if not empty(lista_stanja):

        ob = lista_stanja[n][0]
        koordinate = lista_stanja[n][1]
        old_color = lista_stanja[n][2]

        br = len(lista_stanja[n][1])

        if ob == "cetkica":

            for i in range(br):
                screen.set_at(koordinate[i], old_color[i])
                stack_za_redo.append(lista_stanja.pop())


        elif ob == "linija":

            for i in range(br):

                screen.set_at(koordinate[i], old_color[i])
                stack_za_redo.append(lista_stanja.pop())

        elif ob == "kofica":
            print()

        elif ob == "tekst":
            tekst = lista_stanja[n][1]
            tekst.set_alpha(0)
            stack_za_redo.append(lista_stanja.pop())


def redo():
    n = len(stack_za_redo) - 1
    br = len(stack_za_redo[n][1])

    if not empty(stack_za_redo):

        obel = stack_za_redo[n][0]
        koordinate = lista_stanja[n][1]
        new_color = lista_stanja[n][3]

        if  obel == "cetkica":
            for i in range(br):
                screen.set_at(koordinate[i], new_color[i])
                lista_stanja.append(stack_za_redo.pop())

        elif obel == "linija":
            for i in range (koordinate):
                screen.set_at(koordinate[i], new_color)
                lista_stanja.append(stack_za_redo.pop())

        elif obel == "kofica":
            print()

        elif obel == "tekst":
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 20)
            pisi = font.render(stack_za_redo[n][1], True, (0, 0, 0))
            screen.blit(pisi, pygame.Rect(lista_stanja[n][2], 10, 10), special_flags = pygame.BLEND_RGBA_MULT)
            lista_stanja.append(lista_stanja.pop())