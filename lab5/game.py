import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
NUMBER_OF_BALLS = 5
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
    pos = (0, 0)
    velocity = (0, 0)
    color = RED
    radius = 100

    def __init__(self, pos, velocity, color, radius):
        self.pos = pos
        self.velocity = velocity
        self.color = color
        self.radius = radius

    def new(self):
        """
        generates new ball with random color and radius in random place
        """
        new_ball = create_ball()
        self.pos = new_ball.pos
        self.velocity = new_ball.velocity
        self.color = new_ball.color
        self.radius = new_ball.radius
        return new_ball


def create_ball():
    """
    creates random new object of Ball type
    :return: this object
    """
    radius = randint(10, 100)
    color = COLORS[randint(0, 5)]
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    vx = randint(-1, 1) * SCREEN_WIDTH / randint(5, 10)
    vy = randint(-1, 1) * SCREEN_HEIGHT / randint(5, 10)
    pos = (x, y)
    velocity = (vx, vy)
    ball = Ball(pos, velocity, color, radius)
    return ball


def click(balls, click_event, click_score):
    """
    checks if click was inside a ball
    and removes ball if so
    """
    missed = True
    for i in range(NUMBER_OF_BALLS):
        ball = balls[i]
        ball_x = ball.pos[0]
        ball_y = ball.pos[1]
        radius = ball.radius
        mouse_x = click_event.pos[0]
        mouse_y = click_event.pos[1]
        if (mouse_x - ball_x) * (mouse_x - ball_x) + (mouse_y - ball_y) * (mouse_y - ball_y) <= radius*radius:
            click_score += 10
            balls[i] = create_ball()
            missed = False
            print("Scored")
    if missed:
        click_score -= 5
    return click_score


def balls_move(balls):
    SCREEN.fill(BLACK)
    for i in range(NUMBER_OF_BALLS):
        ball = balls[i]
        x = ball.pos[0]
        y = ball.pos[1]
        vx = ball.velocity[0]
        vy = ball.velocity[1]
        color = ball.color
        pos = (x, y)
        radius = ball.radius
        circle(SCREEN, color, pos, radius)


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
            print('Click!')
            score = click(balls, event, score)
    balls_move(balls)
    pygame.display.update()
    SCREEN.fill(BLACK)
print("Score = ", score)
pygame.quit()
