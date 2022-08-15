import pygame

def brush(x, y, thickness, color, screen):
    pygame.draw.rect(screen, color, pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))    

def rubber(x, y, thickness, screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x-thickness//2, y-thickness//2, thickness, thickness))    
