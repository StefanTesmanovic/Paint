import pygame
from pygame.locals import *
import pygame.locals
from pygame import gfxdraw

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
def floodFill(x, y, oc, nc, screen):
    queue = []
    queue.append((x,y))
    obojeni = []
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        print(x,y)
        obojeni.append((x,y))
        screen.set_at((x, y), nc)
        #screen.fill(nc, ((x, y), (1, 1)))
        #gfxdraw.pixel(screen, x, y, nc)
        if screen.get_at((x+1, y))[:3] == oc and not (x+1, y) in obojeni:
            queue.append((x+1, y))
        if screen.get_at((x-1, y))[:3] == oc and not (x-1, y) in obojeni:
            queue.append((x-1, y))
        if screen.get_at((x, y+1))[:3] == oc and not (x, y+1) in obojeni:
            queue.append((x, y+1))
        if screen.get_at((x, y-1))[:3] == oc and not (x, y-1) in obojeni:
            queue.append((x, y-1))

def pipeta(x, y, screen):
    return screen.get_at((x,y))[:3]
