import pygame
from pygame.draw import *
from pygame.transform import *


def placeflower(surface, pos, angle=0, zoom=1.0):
    sflower = rotozoom(flower, angle, zoom)
    sflower.set_colorkey((113, 200, 55))
    surface.blit(sflower, pos)


def placebush(surface, pos, zoom=1, mirror=False):
    sbush = flip(rotozoom(bush, 0, zoom), mirror, False)
    sbush.set_colorkey((170, 222, 135))
    surface.blit(sbush, pos)


def placekozjol(surface, pos, zoom=1, mirror=False):
    skozjol = flip(rotozoom(kozjol, 0, zoom), mirror, False)
    skozjol.set_colorkey((170, 222, 135))
    surface.blit(skozjol, pos)


pygame.init()

flower = pygame.Surface((70, 35), pygame.SRCALPHA)
flower.fill((113, 200, 55))
flower.set_colorkey((0, 0, 0))
ellipse(flower, (255, 255, 255), (17, 0, 25, 13))
ellipse(flower, (155, 162, 150), (17, 0, 25, 13), 1)
ellipse(flower, (255, 255, 255), (5, 4, 25, 13))
ellipse(flower, (155, 162, 150), (5, 4, 25, 13), 1)
ellipse(flower, (255, 255, 255), (32, 3, 25, 13))
ellipse(flower, (155, 162, 150), (32, 3, 25, 13), 1)
ellipse(flower, (255, 255, 0), (21, 11, 25, 13))
ellipse(flower, (255, 255, 255), (0, 13, 25, 13))
ellipse(flower, (155, 162, 150), (0, 13, 25, 13), 1)
ellipse(flower, (255, 255, 255), (39, 9, 25, 13))
ellipse(flower, (155, 162, 150), (39, 9, 25, 13), 1)
ellipse(flower, (255, 255, 255), (13, 17, 25, 13))
ellipse(flower, (155, 162, 150), (13, 17, 25, 13), 1)
ellipse(flower, (255, 255, 255), (32, 18, 25, 13))
ellipse(flower, (155, 162, 150), (32, 18, 25, 13), 1)

bush = pygame.Surface((300, 300))
bush.fill((170, 222, 135))
circle(bush, (113, 200, 55), (150, 150), 150)
placeflower(bush, (132, 25), angle=0, zoom=1.0)
placeflower(bush, (52, 49), angle=35, zoom=0.75)
placeflower(bush, (66, 108), angle=15, zoom=0.8)
placeflower(bush, (189, 73), angle=-30, zoom=1.5)
placeflower(bush, (90, 165), angle=-15, zoom=2.0)
placeflower(bush, (227, 150), angle=-70, zoom=1.0)

kozjol = pygame.Surface((230, 350))
kozjol.fill((170, 222, 135))
# body
ellipse(kozjol, (255, 255, 255), (147, 17, 66, 40))
ellipse(kozjol, (255, 255, 255), (140, 50, 49, 134))
ellipse(kozjol, (255, 255, 255), (0, 153, 182, 76))
ellipse(kozjol, (255, 255, 255), (11, 191, 25, 48))
ellipse(kozjol, (255, 255, 255), (10, 234, 28, 56))
ellipse(kozjol, (255, 255, 255), (16, 288, 28, 18))
ellipse(kozjol, (255, 255, 255), (46, 212, 27, 60))
ellipse(kozjol, (255, 255, 255), (45, 269, 29, 55))
ellipse(kozjol, (255, 255, 255), (52, 322, 28, 18))
ellipse(kozjol, (255, 255, 255), (114, 182, 25, 52))
ellipse(kozjol, (255, 255, 255), (113, 230, 26, 55))
ellipse(kozjol, (255, 255, 255), (120, 283, 26, 19))
ellipse(kozjol, (255, 255, 255), (137, 208, 28, 64))
ellipse(kozjol, (255, 255, 255), (138, 267, 27, 56))
ellipse(kozjol, (255, 255, 255), (144, 321, 27, 19))
ellipse(kozjol, (255, 255, 255), (144, 321, 27, 19))
# eye
ellipse(kozjol, (229, 128, 255), (161, 20, 31, 27))
ellipse(kozjol, (0, 0, 0), (177, 27, 12, 11))
flare = pygame.Surface((15, 8))
flare.fill((229, 128, 255))
flare.set_colorkey((229, 128, 255))
ellipse(flare, (255, 255, 255), (0, 0, 15, 8))
flare = rotate(flare, -30)
kozjol.blit(flare, (166, 19))
# horns(ears?)
polygon(kozjol, (255, 255, 255), [(155, 26), (148, 24), (139, 17), (132, 6), (132, 2), (132, 8), (135, 18), (142, 27),
                                  (148, 34), (151, 34)])
polygon(kozjol, (255, 255, 255), [(164, 21), (157, 18), (152, 14), (149, 9), (146, 6), (145, 0), (145, 5), (146, 9),
                                  (147, 12), (149, 15), (150, 17), (152, 20), (154, 22), (156, 25)])

FPS = 30
screen = pygame.display.set_mode(size=(800, 1130))

screen.fill((255, 255, 255))
# mountains
polygon(screen, (179, 179, 179), [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195),
                                  (800, 40), (800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576),
                                  (437, 573), (433, 565), (417, 563),
                                  (176, 563), (101, 574), (77, 574), (43, 579), (0, 595)])
# sky
polygon(screen, (175, 221, 233), [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195),
                                  (800, 40), (800, 0), (0, 0)])
# grass
polygon(screen, (170, 222, 135), [(800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573),
                                  (433, 565), (417, 563), (176, 563), (101, 574), (77, 574), (43, 579), (0, 595),
                                  (0, 1130), [800, 1130]])
# black line
polygon(screen, (0, 0, 0), [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195), (800, 40),
                            (800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573),
                            (433, 565), (417, 563), (176, 563),
                            (101, 574), (77, 574), (43, 579), (0, 595)], 2)
# bush
placebush(screen, (516, 776), 1, mirror=False)
# animal
placekozjol(screen, (94, 553))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
