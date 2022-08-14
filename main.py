import pygame

screenw = 500
screenh = 500

screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Paint")
pygame.draw.circle(screen, (100, 100, 100), (50, 50), 50)
pygame.display.flip()

def sejvuj():
    ime = input()
    pygame.image.save(screen, ime)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

pygame.quit()