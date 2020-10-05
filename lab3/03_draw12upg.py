import pygame
from pygame.draw import *
from pygame.transform import *


def placeflower(surface, pos, angle=0, zoom=1.0):
    # pos = (x, y), where x and y are coordinates of left top corner
    # angle: degrees to rotate counterclockwise
    # sflower - flower we are placing
    sflower = rotozoom(flower, angle, zoom)
    sflower.set_colorkey(BLACK)
    surface.blit(sflower, pos)


def placebush(surface, pos, zoom=1.0, mirror=False):
    # pos = (x, y), where x and y are coordinates of left top corner
    # mirror: if True - flip vertically
    # sbush - bush we are placing
    sbush = flip(rotozoom(bush, 0, zoom), mirror, False)
    sbush.set_colorkey(LIGHT_GREEN)
    surface.blit(sbush, pos)


def placekozjol(surface, pos, zoom=1.0, mirror=False):
    # pos = (x, y), where x and y are coordinates of left top corner
    # mirror: if True - flip vertically
    # skozjol - kozjol we are placing
    skozjol = flip(rotozoom(kozjol, 0, zoom), mirror, False)
    skozjol.set_colorkey(LIGHT_GREEN)
    surface.blit(skozjol, pos)


quality = 10

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (155, 162, 150)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (170, 222, 135)
BLUE = (175, 221, 233)

flower = pygame.Surface((70 * quality, 35 * quality))
flower.fill(BLACK)
ellipse(flower, WHITE, (17 * quality, 0 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (17 * quality, 0 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, WHITE, (5 * quality, 4 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (5 * quality, 4 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, WHITE, (32 * quality, 3 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (32 * quality, 3 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, YELLOW, (21 * quality, 11 * quality, 25 * quality, 13 * quality))
ellipse(flower, WHITE, (0 * quality, 13 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (0 * quality, 13 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, WHITE, (39 * quality, 9 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (39 * quality, 9 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, WHITE, (13 * quality, 17 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (13 * quality, 17 * quality, 25 * quality, 13 * quality), 1 * quality)
ellipse(flower, WHITE, (32 * quality, 18 * quality, 25 * quality, 13 * quality))
ellipse(flower, GREY, (32 * quality, 18 * quality, 25 * quality, 13 * quality), 1 * quality)

bush = pygame.Surface((300 * quality, 300 * quality))
bush.fill(LIGHT_GREEN)
circle(bush, (113, 200, 55), (150 * quality, 150 * quality), 150 * quality)
placeflower(bush, (132 * quality, 25 * quality), angle=0, zoom=1.0)
placeflower(bush, (52 * quality, 49 * quality), angle=35, zoom=0.75)
placeflower(bush, (66 * quality, 108 * quality), angle=15, zoom=0.8)
placeflower(bush, (189 * quality, 73 * quality), angle=-30, zoom=1.5)
placeflower(bush, (90 * quality, 165 * quality), angle=-15, zoom=2.0)
placeflower(bush, (227 * quality, 150 * quality), angle=-70, zoom=1.0)

kozjol = pygame.Surface((230 * quality, 350 * quality))
kozjol.fill(LIGHT_GREEN)
# body
ellipse(kozjol, WHITE, (147 * quality, 17 * quality, 66 * quality, 40 * quality))
ellipse(kozjol, WHITE, (140 * quality, 50 * quality, 49 * quality, 134 * quality))
ellipse(kozjol, WHITE, (0 * quality, 153 * quality, 182 * quality, 76 * quality))
ellipse(kozjol, WHITE, (11 * quality, 191 * quality, 25 * quality, 48 * quality))
ellipse(kozjol, WHITE, (10 * quality, 234 * quality, 28 * quality, 56 * quality))
ellipse(kozjol, WHITE, (16 * quality, 288 * quality, 28 * quality, 18 * quality))
ellipse(kozjol, WHITE, (46 * quality, 212 * quality, 27 * quality, 60 * quality))
ellipse(kozjol, WHITE, (45 * quality, 269 * quality, 29 * quality, 55 * quality))
ellipse(kozjol, WHITE, (52 * quality, 322 * quality, 28 * quality, 18 * quality))
ellipse(kozjol, WHITE, (114 * quality, 182 * quality, 25 * quality, 52 * quality))
ellipse(kozjol, WHITE, (113 * quality, 230 * quality, 26 * quality, 55 * quality))
ellipse(kozjol, WHITE, (120 * quality, 283 * quality, 26 * quality, 19 * quality))
ellipse(kozjol, WHITE, (137 * quality, 208 * quality, 28 * quality, 64 * quality))
ellipse(kozjol, WHITE, (138 * quality, 267 * quality, 27 * quality, 56 * quality))
ellipse(kozjol, WHITE, (144 * quality, 321 * quality, 27 * quality, 19 * quality))
ellipse(kozjol, WHITE, (144 * quality, 321 * quality, 27 * quality, 19 * quality))
# eye
ellipse(kozjol, (229, 128, 255), (161 * quality, 20 * quality, 31 * quality, 27 * quality))
ellipse(kozjol, BLACK, (177 * quality, 27 * quality, 12 * quality, 11 * quality))
flare = pygame.Surface((15 * quality, 8 * quality))
flare.fill((229, 128, 255))
flare.set_colorkey((229, 128, 255))
ellipse(flare, WHITE, (0 * quality, 0 * quality, 15 * quality, 8 * quality))
flare = rotate(flare, -30)
kozjol.blit(flare, (166 * quality, 19 * quality))
# horns(ears?)
polygon(kozjol, WHITE,
        [(155 * quality, 26 * quality), (148 * quality, 24 * quality), (139 * quality, 17 * quality),
         (132 * quality, 6 * quality), (132 * quality, 2 * quality), (132 * quality, 8 * quality),
         (135 * quality, 18 * quality), (142 * quality, 27 * quality), (148 * quality, 34 * quality),
         (151 * quality, 34 * quality)])
polygon(kozjol, WHITE,
        [(164 * quality, 21 * quality), (157 * quality, 18 * quality), (152 * quality, 14 * quality),
         (149 * quality, 9 * quality), (146 * quality, 6 * quality), (145 * quality, 0 * quality),
         (145 * quality, 5 * quality), (146 * quality, 9 * quality), (147 * quality, 12 * quality),
         (149 * quality, 15 * quality), (150 * quality, 17 * quality), (152 * quality, 20 * quality),
         (154 * quality, 22 * quality), (156 * quality, 25 * quality)])

FPS = 30
screen = pygame.display.set_mode(size=(800, 1130))

screen.fill(WHITE)
# mountains
polygon(screen, GREY, [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195),
                                  (800, 40), (800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576),
                                  (437, 573), (433, 565), (417, 563),
                                  (176, 563), (101, 574), (77, 574), (43, 579), (0, 595)])
# sky
polygon(screen, BLUE, [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195),
                                  (800, 40), (800, 0), (0, 0)])
# grass
polygon(screen, LIGHT_GREEN, [(800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573),
                                  (433, 565), (417, 563), (176, 563), (101, 574), (77, 574), (43, 579), (0, 595),
                                  (0, 1130), [800, 1130]])
# black line
polygon(screen, BLACK, [(0, 347), (95, 115), (165, 276), (272, 148), (473, 450), (619, 138), (667, 195), (800, 40),
                            (800, 665), (466, 665), (445, 656), (445, 600), (441, 597), (441, 576), (437, 573),
                            (433, 565), (417, 563), (176, 563),
                            (101, 574), (77, 574), (43, 579), (0, 595)], 2)
# bushes
placebush(screen, (-10, 578), 0.23/quality, mirror=False)
placebush(screen, (563, 667), 0.23/quality, mirror=False)
placebush(screen, (516, 898), 0.6/quality, mirror=False)
placebush(screen, (690, 607), 0.36/quality, mirror=True)
placebush(screen, (679, 734), 0.6/quality, mirror=True)
placebush(screen, (760, 1030), 0.32/quality, mirror=True)
# animals
placekozjol(screen, (283, 465), 0.4/quality, mirror=False)
placekozjol(screen, (172, 583), 0.4/quality, mirror=False)
placekozjol(screen, (325, 639), 0.4/quality, mirror=True)

placekozjol(screen, (665, 593), 1.2/quality, mirror=True)
placekozjol(screen, (-280, 715), 2.2/quality, mirror=False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
