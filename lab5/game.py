import pygame
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
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
NUMBER_OF_BALLS = 3
MAX_SPEED = 500
MIN_SPEED = 400
MAX_RADIUS = 70
MIN_RADIUS = 20
MAX_TIME = 2
MIN_TIME = 1
IVANOV = pygame.image.load(os.path.join('ivanov.png'))
PKOZHEVN = pygame.image.load(os.path.join('pkozhevn.png'))
IVANOV.set_colorkey(WHITE)
PKOZHEVN.set_colorkey(WHITE)
IVANOV = pygame.transform.rotozoom(IVANOV, 0, 0.5)
PKOZHEVN = pygame.transform.rotozoom(PKOZHEVN, 0, 0.16)
IVANOV = pygame.transform.flip(IVANOV, True, False)
PKOZHEVN = pygame.transform.flip(PKOZHEVN, True, False)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Ball:
    def __init__(self, pos, velocity, color, radius, life_time, time_left):
        self.pos = pos
        self.velocity = velocity
        self.color = color
        self.radius = radius
        self.life_time = life_time
        self.time_left = time_left

    def move(self):
        """
        Moves a ball, changes its color and time_left.
        If the ball is dead a new ball is created
        :return: None
        """
        time_left = self.time_left
        life_time = self.life_time
        x = self.pos[0]
        y = self.pos[1]
        vx = self.velocity[0]
        vy = self.velocity[1]
        radius = self.radius
        time_left -= 1 / FPS
        color = ((1 - time_left / life_time) * 255, 0, (time_left / life_time) * 255)  # blue to red gradient
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
        self.color = color
        if time_left <= 0:
            self.new()

    def draw(self):
        """
        Draws a ball
        :return: None
        """
        color = self.color
        pos = self.pos
        radius = self.radius
        pygame.draw.circle(SCREEN, color, pos, radius)

    def is_inside(self, pos):
        """
        Checks if pos is inside self
        :param pos: (x, y)
        :return: True if inside, False if not
        """
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
        self.life_time = new_ball.life_time
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
            self.surface = pygame.transform.flip(self.surface, True, False)
            y = randint(0, SCREEN_HEIGHT - 130)
            x = SCREEN_WIDTH
            vx = -vx
        if x <= -100:
            self.surface = pygame.transform.flip(self.surface, True, False)
            y = randint(0, SCREEN_HEIGHT - 130)
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

    def is_inside(self, pos):
        x = self.pos[0]
        y = self.pos[1]
        surface = self.surface
        if x + surface.get_width() > pos[0] > x and y + surface.get_height() > pos[1] > y:
            color_at_pos = self.surface.get_at((pos[0] - x, pos[1] - y))
            if color_at_pos[0] <= 5 and color_at_pos[1] <= 5 and color_at_pos[2] <= 5:
                return False
            else:
                return True
        else:
            return False


def create_ball():
    """
    creates random new object of Ball type
    :return: this object
    """
    radius = randint(MIN_RADIUS, MAX_RADIUS)
    color = (0, 0, 255)
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    vx = randint(-1, 1) * randint(MIN_SPEED, MAX_SPEED)
    vy = randint(-1, 1) * randint(MIN_SPEED, MAX_SPEED)
    life_time = uniform(MIN_TIME, MAX_TIME)
    time_left = life_time
    pos = (x, y)
    velocity = (vx, vy)
    ball = Ball(pos, velocity, color, radius, life_time, time_left)
    return ball


def click(click_balls, click_lectors, click_event, click_score):
    """
    checks if click was inside a ball
    and removes ball if so
    """
    missed = True
    for click_i in range(len(click_lectors)):
        if missed:
            lector = lectors[len(click_lectors) - click_i - 1]
            if lector.is_inside(click_event.pos):
                click_score += 2
                for other_lector in lectors:
                    vx = -other_lector.velocity[0]
                    vy = other_lector.velocity[1]
                    other_lector.velocity = (vx, vy)
                    other_lector.surface = pygame.transform.flip(other_lector.surface, True, False)
                missed = False

    for click_i in range(len(click_balls)):
        if missed:
            ball = click_balls[len(click_balls) - click_i - 1]
            radius = ball.radius
            if ball.is_inside(click_event.pos):
                click_score += int(10 * MIN_RADIUS / radius)
                click_balls[len(click_balls) - click_i - 1] = create_ball()
                missed = False
    if missed:
        click_score -= 10
    return click_score


def main_frame(frame_balls, frame_lectors, frame_score):
    SCREEN.fill(BLACK)
    for frame_i in range(len(frame_balls)):
        ball = frame_balls[frame_i]
        ball.move()
        ball.draw()
    for frame_i in range(len(frame_lectors)):
        lector = lectors[frame_i]
        lector.move()
        lector.draw()
    font = pygame.font.Font(None, 40)
    score_surface = font.render('Score: ' + str(frame_score), True, WHITE)
    name_surface = font.render('Player name: ' + PLAYER_NAME, True, WHITE)
    score_surface.set_colorkey(BLACK)
    name_surface.set_colorkey(BLACK)
    SCREEN.blit(score_surface, (0, 0))
    SCREEN.blit(name_surface, (0, 40))


def player_name_frame():
    SCREEN.fill(BLACK)
    font = pygame.font.Font(None, 80)
    name_surface = font.render('Player name: ' + PLAYER_NAME, True, WHITE)
    name_surface.set_colorkey(BLACK)
    SCREEN.blit(name_surface, (0, 0))


def keyboard_input(key_down_event):
    letter = ''
    key = key_down_event.key
    if 48 <= key <= 57:
        letter = chr(key)
    if 97 <= key <= 122:
        letter = key_down_event.unicode
    return PLAYER_NAME + letter


ivanov_surf = Lector((-100, SCREEN_HEIGHT - 130), (2 * MAX_SPEED, 0), IVANOV)
pkozhevn_surf = Lector((SCREEN_WIDTH, 0), (2 * MAX_SPEED, 0), PKOZHEVN)
lectors = [ivanov_surf, pkozhevn_surf]

clock = pygame.time.Clock()
score = 0
finished = False
name_received = False
balls = []
for i in range(NUMBER_OF_BALLS):
    balls.append(create_ball())
file = open('leaderboard.txt', 'r')

for line in file:
    line = line.rstrip()

PLAYER_NAME = ''
while not (name_received or finished):
    clock.tick(FPS)
    for event in pygame.event.get():
        if not name_received:
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name_received = True
                else:
                    PLAYER_NAME = keyboard_input(event)
    player_name_frame()
    pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(balls, lectors, event, score)
    main_frame(balls, lectors, score)
    pygame.display.update()
print("Score =", score)

pygame.quit()
