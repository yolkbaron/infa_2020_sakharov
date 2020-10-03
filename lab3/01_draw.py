import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode(size=(1920, 1080))

screen.fill((255, 255, 255))
circle(screen, (255, 255, 0), (960, 540), 400)  # head
circle(screen, (0, 0, 0), (960, 540), 400, 3)
circle(screen, (255, 0, 0), (1160, 440), 60)  # right eye
circle(screen, (0, 0, 0), (1160, 440), 30)
circle(screen, (0, 0, 0), (1160, 440), 60, 3)
circle(screen, (255, 0, 0), (760, 440), 80)  # left eye
circle(screen, (0, 0, 0), (760, 440), 40)
circle(screen, (0, 0, 0), (760, 440), 80, 3)
line(screen, (0, 0, 0), (710, 740), (1210, 740), 100)  # mouth
polygon(screen, (0, 0, 0), [(540 - 21/2, 200 + 37/2), (540 + 21/2, 200 - 37/2), (910 + 21/2, 410 - 37/2),
                            (910 - 21/2, 410 + 37/2)])  # brows
polygon(screen, (0, 0, 0), [(1920-(540 - 13/2), 280 + 37/2), (1920 - (540 + 13/2), 280 - 37/2),
                            (1920 - (910 + 13/2), 410 - 37/2), (1920 - (910 - 13/2), 410 + 37/2)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
