import pygame

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