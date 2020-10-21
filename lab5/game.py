import pygame
from pygame.draw import *
from pygame.transform import *
import os
from random import uniform
from random import randint

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 60
DIFFICULTY = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
NUMBER_OF_BALLS = 3
MAX_SPEED = 200
MIN_SPEED = 100
MAX_RADIUS = 70
MIN_RADIUS = 20
MAX_TIME = 1
MIN_TIME = 0.5
IVANOV = pygame.image.load(os.path.join('ivanov.png'))
PKOZHEVN = pygame.image.load(os.path.join('pkozhevn.png'))
IVANOV.set_colorkey(WHITE)
PKOZHEVN.set_colorkey(WHITE)
IVANOV = rotozoom(IVANOV, 0, 0.5)
PKOZHEVN = rotozoom(PKOZHEVN, 0, 0.16)
IVANOV = flip(IVANOV, True, False)
PKOZHEVN = flip(PKOZHEVN, True, False)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Ball:
    def __init__(self, pos, velocity, color, radius, time_left):
        self.pos = pos
        self.velocity = velocity
        self.color = color
        self.radius = radius
        self.time_left = time_left

    def move(self):
        time_left = self.time_left
        x = self.pos[0]
        y = self.pos[1]
        vx = self.velocity[0]
        vy = self.velocity[1]
        radius = self.radius
        time_left -= 1 / FPS
        x += int(vx / FPS)
        y += int(vy / FPS)
        if x >= SCREEN_WIDTH - radius:
            x = SCREEN_WIDTH - radius
            vx = -vx
        if x <= radius:
            x = radius
            vx = -vx
        if y >= SCREEN_HEIGHT - radius:
            y = SCREEN_HEIGHT - radius
            vy = -vy
        if y <= radius:
            y = radius
            vy = -vy
        self.time_left = time_left
        pos = (x, y)
        velocity = (vx, vy)
        self.pos = pos
        self.velocity = velocity
        if time_left <= 0:
            self.new()

    def draw(self):
        color = self.color
        pos = self.pos
        radius = self.radius
        circle(SCREEN, color, pos, radius)

    def is_inside(self, pos):
        ball_x = self.pos[0]
        ball_y = self.pos[1]
        radius = self.radius
        mouse_x = pos[0]
        mouse_y = pos[1]
        if (mouse_x - ball_x) * (mouse_x - ball_x) + (mouse_y - ball_y) * (mouse_y - ball_y) <= radius * radius:
            return True
        else:
            return False

    def new(self):
        """
        generates new ball with random color and radius in random place
        """
        new_ball = create_ball()
        self.pos = new_ball.pos
        self.velocity = new_ball.velocity
        self.color = new_ball.color
        self.radius = new_ball.radius
        self.time_left = new_ball.time_left
        return new_ball


class Lector:
    def __init__(self, pos, velocity, surface):
        self.pos = pos
        self.velocity = velocity
        self.surface = surface

    def move(self):
        x = self.pos[0]
        y = self.pos[1]
        vx = self.velocity[0]
        vy = self.velocity[1]
        x += int(vx / FPS)
        y += int(vy / FPS)
        if x >= SCREEN_WIDTH:
            self.surface = flip(self.surface, True, False)
            y = randint(0, SCREEN_HEIGHT-130)
            x = SCREEN_WIDTH
            vx = -vx
        if x <= -100:
            self.surface = flip(self.surface, True, False)
            y = randint(0, SCREEN_HEIGHT-130)
            x = -100
            vx = -vx
        pos = (x, y)
        velocity = (vx, vy)
        self.pos = pos
        self.velocity = velocity

    def draw(self):
        pos = self.pos
        surface = self.surface
        SCREEN.blit(surface, pos)


def create_ball():
    """
    creates random new object of Ball type
    :return: this object
    """
    radius = randint(MIN_RADIUS, MAX_RADIUS)
    color = COLORS[randint(0, 5)]
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    vx = randint(-1, 1) * randint(MIN_SPEED, MAX_SPEED) * DIFFICULTY
    vy = randint(-1, 1) * randint(MIN_SPEED, MAX_SPEED) * DIFFICULTY
    time_left = uniform(MIN_TIME, MAX_TIME)
    pos = (x, y)
    velocity = (vx, vy)
    ball = Ball(pos, velocity, color, radius, time_left)
    return ball


def click(click_balls, click_lectors, click_event, click_score):
    """
    checks if click was inside a ball
    and removes ball if so
    """
    missed = True
    for i in range(len(click_lectors)):
        if missed:
            pass

    for i in range(len(click_balls)):
        if missed:
            ball = click_balls[len(click_balls) - i - 1]
            radius = ball.radius
            if ball.is_inside(click_event.pos):
                click_score += int(10*MIN_RADIUS/radius)
                click_balls[len(click_balls) - i - 1] = create_ball()
                missed = False
                print("Scored")
    if missed:
        click_score -= 5
    return click_score


def frame(frame_balls, frame_lectors):
    SCREEN.fill(BLACK)
    for i in range(len(frame_balls)):
        ball = frame_balls[i]
        ball.move()
        ball.draw()
    for i in range(len(frame_lectors)):
        lector = lectors[i]
        lector.move()
        lector.draw()


ivanov_surf = Lector((-100, SCREEN_HEIGHT-130), (4*MAX_SPEED, 0), IVANOV)
pkozhevn_surf = Lector((SCREEN_WIDTH, 0), (4*MAX_SPEED, 0), PKOZHEVN)
lectors = [ivanov_surf, pkozhevn_surf]
score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = []
for i in range(NUMBER_OF_BALLS):
    balls.append(create_ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(balls, lectors, event, score)
    frame(balls, lectors)
    pygame.display.update()
print("Score = ", score)
pygame.quit()
