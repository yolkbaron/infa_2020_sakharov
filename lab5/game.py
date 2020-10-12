import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, pos, velocity, color, radius):
        self.pos = pos
        self.velocity = velocity
        self.color = color
        self.radius = radius


def ball_generator():
    """
    draws a new ball with random color and radius in random place
    """
    global x, y, r
    for i in range(randint(1, 10)):
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(click_event, click_score):
    """
    checks if click was inside a ball
    """
    if (click_event.pos[0] - x) ** 2 + (click_event.pos[1] - y) ** 2 <= r ** 2:
        click_score += 1
    return click_score


score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            score = click(event, score)
    ball_generator()
    pygame.display.update()
    screen.fill(BLACK)
print("Score = ", score)
pygame.quit()
