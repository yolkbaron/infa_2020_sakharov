import pygame
from pygame.draw import *
from pygame.transform import *


def placeflower(surface, pos, angle=0, zoom=1.0):
    sflower = rotozoom(flower, angle, zoom)
    sflower.set_colorkey((0, 0, 0))
    surface.blit(sflower, pos)


def placebush(surface, pos, zoom=1.0, mirror=False):
    sbush = flip(rotozoom(bush, 0, zoom), mirror, False)
    sbush.set_colorkey((170, 222, 135))
    surface.blit(sbush, pos)


def placekozjol(surface, pos, zoom=1.0, mirror=False):
    skozjol = flip(rotozoom(kozjol, 0, zoom), mirror, False)
    skozjol.set_colorkey((170, 222, 135))
    surface.blit(skozjol, pos)


quality = 10

pygame.init()

flower = pygame.Surface((70*quality, 35*quality))
flower.fill((0, 0, 0))
ellipse(flower, (255, 255, 255), (17*quality, 0*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (17*quality, 0*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 255), (5*quality, 4*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (5*quality, 4*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 255), (32*quality, 3*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (32*quality, 3*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 0), (21*quality, 11*quality, 25*quality, 13*quality))
ellipse(flower, (255, 255, 255), (0*quality, 13*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (0*quality, 13*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 255), (39*quality, 9*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (39*quality, 9*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 255), (13*quality, 17*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (13*quality, 17*quality, 25*quality, 13*quality), 1*quality)
ellipse(flower, (255, 255, 255), (32*quality, 18*quality, 25*quality, 13*quality))
ellipse(flower, (155, 162, 150), (32*quality, 18*quality, 25*quality, 13*quality), 1*quality)

bush = pygame.Surface((300*quality, 300*quality))
bush.fill((170, 222, 135))
circle(bush, (113, 200, 55), (150*quality, 150*quality), 150*quality)
placeflower(bush, (132*quality, 25*quality), angle=0, zoom=1.0)
placeflower(bush, (52*quality, 49*quality), angle=35, zoom=0.75)
placeflower(bush, (66*quality, 108*quality), angle=15, zoom=0.8)
placeflower(bush, (189*quality, 73*quality), angle=-30, zoom=1.5)
placeflower(bush, (90*quality, 165*quality), angle=-15, zoom=2.0)
placeflower(bush, (227*quality, 150*quality), angle=-70, zoom=1.0)

kozjol = pygame.Surface((230*quality, 350*quality))
kozjol.fill((170, 222, 135))
# body
ellipse(kozjol, (255, 255, 255), (147*quality, 17*quality, 66*quality, 40*quality))
ellipse(kozjol, (255, 255, 255), (140*quality, 50*quality, 49*quality, 134*quality))
ellipse(kozjol, (255, 255, 255), (0*quality, 153*quality, 182*quality, 76*quality))
ellipse(kozjol, (255, 255, 255), (11*quality, 191*quality, 25*quality, 48*quality))
ellipse(kozjol, (255, 255, 255), (10*quality, 234*quality, 28*quality, 56*quality))
ellipse(kozjol, (255, 255, 255), (16*quality, 288*quality, 28*quality, 18*quality))
ellipse(kozjol, (255, 255, 255), (46*quality, 212*quality, 27*quality, 60*quality))
ellipse(kozjol, (255, 255, 255), (45*quality, 269*quality, 29*quality, 55*quality))
ellipse(kozjol, (255, 255, 255), (52*quality, 322*quality, 28*quality, 18*quality))
ellipse(kozjol, (255, 255, 255), (114*quality, 182*quality, 25*quality, 52*quality))
ellipse(kozjol, (255, 255, 255), (113*quality, 230*quality, 26*quality, 55*quality))
ellipse(kozjol, (255, 255, 255), (120*quality, 283*quality, 26*quality, 19*quality))
ellipse(kozjol, (255, 255, 255), (137*quality, 208*quality, 28*quality, 64*quality))
ellipse(kozjol, (255, 255, 255), (138*quality, 267*quality, 27*quality, 56*quality))
ellipse(kozjol, (255, 255, 255), (144*quality, 321*quality, 27*quality, 19*quality))
ellipse(kozjol, (255, 255, 255), (144*quality, 321*quality, 27*quality, 19*quality))
# eye
ellipse(kozjol, (229, 128, 255), (161*quality, 20*quality, 31*quality, 27*quality))
ellipse(kozjol, (0, 0, 0), (177*quality, 27*quality, 12*quality, 11*quality))
flare = pygame.Surface((15*quality, 8*quality))
flare.fill((229, 128, 255))
flare.set_colorkey((229, 128, 255))
ellipse(flare, (255, 255, 255), (0*quality, 0*quality, 15*quality, 8*quality))
flare = rotate(flare, -30)
kozjol.blit(flare, (166*quality, 19*quality))
# horns(ears?)
polygon(kozjol, (255, 255, 255), [(155*quality, 26*quality), (148*quality, 24*quality), (139*quality, 17*quality),
                                  (132*quality, 6*quality), (132*quality, 2*quality), (132*quality, 8*quality),
                                  (135*quality, 18*quality), (142*quality, 27*quality), (148*quality, 34*quality),
                                  (151*quality, 34*quality)])
polygon(kozjol, (255, 255, 255), [(164*quality, 21*quality), (157*quality, 18*quality), (152*quality, 14*quality),
                                  (149*quality, 9*quality), (146*quality, 6*quality), (145*quality, 0*quality),
                                  (145*quality, 5*quality), (146*quality, 9*quality), (147*quality, 12*quality),
                                  (149*quality, 15*quality), (150*quality, 17*quality), (152*quality, 20*quality),
                                  (154*quality, 22*quality), (156*quality, 25*quality)])

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
placebush(screen, (516, 776), 1/quality, mirror=False)
# animal
placekozjol(screen, (94, 553), 1/quality, mirror=False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
