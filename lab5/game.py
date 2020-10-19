import pygame
from pygame.draw import *
from random import uniform
from random import randint


pygame.init()

FPS = 60
DIFFICULTY = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
number_of_balls = 3
MAX_RADIUS = 70
MIN_RADIUS = 20
MAX_TIME = 1
MIN_TIME = 0.5
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


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


def create_ball():
    """
    creates random new object of Ball type
    :return: this object
    """
    radius = randint(MIN_RADIUS, MAX_RADIUS)
    color = COLORS[randint(0, 5)]
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    vx = randint(-1, 1) * randint(100, 200) * DIFFICULTY
    vy = randint(-1, 1) * randint(100, 200) * DIFFICULTY
    time_left = uniform(MIN_TIME, MAX_TIME)
    pos = (x, y)
    velocity = (vx, vy)
    ball = Ball(pos, velocity, color, radius, time_left)
    return ball


def click(click_balls, click_event, click_score):
    """
    checks if click was inside a ball
    and removes ball if so
    """
    missed = True
    for i in range(len(click_balls)):
        ball = click_balls[i]
        ball_x = ball.pos[0]
        ball_y = ball.pos[1]
        radius = ball.radius
        mouse_x = click_event.pos[0]
        mouse_y = click_event.pos[1]
        if (mouse_x - ball_x) * (mouse_x - ball_x) + (mouse_y - ball_y) * (mouse_y - ball_y) <= radius*radius:
            click_score += 10
            click_balls[i] = create_ball()
            missed = False
            print("Scored")
    if missed:
        click_score -= 5
    return click_score


def frame(frame_balls):
    SCREEN.fill(BLACK)
    for i in range(len(frame_balls)):
        ball = frame_balls[i]
        ball.move()
        color = ball.color
        pos = ball.pos
        radius = ball.radius
        circle(SCREEN, color, pos, radius)


score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = []
for i in range(number_of_balls):
    balls.append(create_ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(balls, event, score)
    frame(balls)
    pygame.display.update()
print("Score = ", score)
pygame.quit()