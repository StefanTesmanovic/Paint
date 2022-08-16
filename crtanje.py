import pygame
from main import lista_stanja
from main import screen


def crtanjeLinija(start, end, boja = (0, 0, 0)):
    n = len(lista_stanja) - 1
    stara_boja = []

    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)

    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
    
    #boja:
        stara_boja.append(screen.get_at((x, y))[:3])
        screen.set_at((x, y), boja)
    #koordinate:
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()

    lista_stanja[n][0] = "linija"
    lista_stanja[n][1] = points
    lista_stanja[n][2] = stara_boja
    lista_stanja[n][3] = boja

    return points   

def tekst(x, y):
    running = True
    txt = ""
    n = len(lista_stanja) - 1
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)

    while running:
        slovo = pygame.key.get_pressed
        pom = 0
        if slovo.type == pygame.KEYDOWN:
            if slovo.key == pygame.K_KP_ENTER:
                running = False
            else:
                txt += slovo
                pisi = font.render(slovo, True, (0, 0, 0))
                screen.blit(pisi, pygame.Rect(x + pom, y, 10, 10), special_flags = pygame.BLEND_RGBA_MULT)
                pom += 1

    lista_stanja[n][0] ="tekst"
    lista_stanja[n][1] = txt
    lista_stanja[n][2] = (x, y)

def brush(x, y, thickness, color, screen):
    pygame.draw.rect(screen, color, pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))    

def rubber(x, y, thickness, screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))    

def floodFill(x, y, oc, nc, screen):
    if screen.get_at((x, y))[:3] == oc:
        screen.set_at((x,y), nc)
        floodFill(x-1, y, oc, nc, screen)
        floodFill(x+1, y, oc, nc, screen)
        floodFill(x, y-1, oc, nc, screen)
        floodFill(x, y+1, oc, nc, screen)
    pass
