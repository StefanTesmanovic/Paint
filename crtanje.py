import pygame
from pygame.locals import *
import pygame.locals

def brush(x, y, thickness, color, screen):
    pygame.draw.rect(screen, color, pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))
    lista = []
    a = x-thickness//2
    b = y-thickness//2
    boja = []
    boja = screen.get_at((a, b))[:3]  
    
    for i in range(thickness):
        for j in range(thickness):
            if color != screen.get_at((a+i*thickness, b+j))[:3]:
                boja = screen.get_at((a+i*thickness, b+j))[:3]
            lista.append((a+i*thickness, b+j, boja))
    return lista            


def rubber(x, y, thickness, screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))    
    
    lista = []
    a = x-thickness//2
    b = y-thickness//2
    boja = []
    boja = screen.get_at((a, b))[:3]  
    
    for i in range(thickness):
        for j in range(thickness):
            if (255, 255, 255) != screen.get_at((a+i*thickness, b+j))[:3]:
                boja = screen.get_at((a+i*thickness, b+j))[:3]
            lista.append((a+i*thickness, b+j, boja))
    return lista

def crtanjeLinija(start, end, boja, lista_stanja, screen):
    n = len(lista_stanja) - 1
    lista = []
    oc = screen.get_at(start)[:3]
    pygame.draw.line(screen, boja, start, end)
    lista.append("linija")
    lista.append((start, end, oc))
    '''(x1, y1) = start
    (x2, y2) = end
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
        points.reverse()'''

    #lista_stanja[n][0] = "linija"
    #lista_stanja[n][1] = points
    #lista_stanja[n][2] = stara_boja
    #lista_stanja[n][3] = boja
 

def tekst(x, y, screen):
    running = True
    pygame.font.init()
    font = pygame.font.SysFont("Consolas", 20)

    pom = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    running = False
                else:
                    try:
                        pisi = font.render(chr(event.key), True, (0, 255, 255))
                        screen.blit(pisi, (x+pom*10, y))
                        pygame.display.flip()
                        pom += 1
                    except:
                        continue

