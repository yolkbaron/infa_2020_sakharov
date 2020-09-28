import pygame
from pygame.draw import *

#define kozjol(x, y, size = 1, mirror = False):
    


pygame.init()

FPS = 30
screen = pygame.display.set_mode(size = (794, 1123))

screen.fill((255, 255, 255))
polygon(screen, (192, 192, 192), [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195), (794, 40), (794, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573), (433, 565), (417, 563), (176, 563), (101, 574), (77, 574), (43, 579), (0, 595)])
polygon(screen, (0, 0, 0), [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195), (794, 40), (794, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573), (433, 565), (417, 563), (176, 563), (101, 574), (77, 574), (43, 579), (0, 595)], 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
