import pygame

screenw = 500
screenh = 500

screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Paint")



running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
