import random as rnd
import math
import pygame

FPS = 60
GRAVITY_ACCELERATION = 9.8  # Ускорение свободного падения для снаряда.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCALE = SCREEN_WIDTH / 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Cannon:
    max_power = 3
    min_v = 5 * SCALE
    length = 50
    thickness = 20
    height = 50
    cannon_v = 5 * SCALE

    def __init__(self, x, y):
        self.power = 0
        self.on = False
        self.x = x
        self.y = y
        self.shell_num = 100
        self.direction = math.pi / 4
        self.color = BLACK
        self.moving_dest = "NONE"

    def aim(self, pos):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param pos: tuple (x, y) of mouse coords
        :return: None
        """
        x = pos[0] - self.x
        y = self.y - pos[1] - Cannon.height
        if x != 0:
            direction = math.atan(y / x)
        else:
            direction = math.pi / 2
        if x >= 0:
            self.direction = max(0, direction)
        else:
            self.direction = min(math.pi, direction + math.pi)
        if self.on:
            self.power += Cannon.max_power / FPS
        if self.power > Cannon.max_power:
            self.power = Cannon.max_power

    def fire(self):
        """
        Creates Shell object (if there are still shells left)
        flying to angle from self.direction
        with speed that depends from self.power
        :return: экземпляр снаряда типа Shell
        """
        if self.shell_num > 0:
            self.shell_num -= 1
            length = Cannon.length
            x, y = (self.x + length * math.cos(self.direction), self.y - length * math.sin(self.direction) - Cannon.height/2)
            vx = Cannon.min_v * (self.power + 1) * math.cos(self.direction)
            vy = Cannon.min_v * (self.power + 1) * math.sin(self.direction)
            projectile = Shell(x, y, vx, -vy, self.color)
            return projectile

    def draw(self):
        """
        Draws a cannon
        :return:
        """
        self.color = (self.power * 255 / Cannon.max_power, 0, 0)
        half = Cannon.thickness / 2
        length = Cannon.length
        cos = math.cos(self.direction)
        sin = math.sin(self.direction)
        pos1 = (self.x - half * sin, self.y - half * cos - Cannon.height/2)
        pos2 = (self.x - half * sin + length * cos, self.y - half * cos - length * sin - Cannon.height/2)
        pos3 = (self.x + half * sin + length * cos, self.y + half * cos - length * sin - Cannon.height/2)
        pos4 = (self.x + half * sin, self.y + half * cos - Cannon.height/2)
        pos5 = (self.x - Cannon.height/2, self.y)
        pos6 = (self.x - Cannon.height/2, self.y - Cannon.height)
        pos7 = (self.x + Cannon.height/2, self.y - Cannon.height)
        pos8 = (self.x + Cannon.height/2, self.y)
        pygame.draw.polygon(screen, self.color, [pos1, pos2, pos3, pos4])
        pygame.draw.polygon(screen, BLACK, [pos5, pos6, pos7, pos8])


    def move(self, dt=1 / FPS):
        if self.moving_dest == "LEFT" and self.x > Cannon.height/2:
            self.x -= Cannon.cannon_v * dt
        elif self.moving_dest == "RIGHT" and self.x < SCREEN_WIDTH - Cannon.height/2:
            self.x += Cannon.cannon_v * dt


class Shell:
    standard_radius = 10

    def __init__(self, x, y, vx, vy, color):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Shell.standard_radius
        self.color = color
        self.is_alive = True

    def move(self, dt=1 / FPS):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        ax, ay = 0, GRAVITY_ACCELERATION * SCALE
        self.x += self.vx * dt + ax * (dt ** 2) / 2
        self.y += self.vy * dt + ay * (dt ** 2) / 2
        self.vx += ax * dt
        self.vy += ay * dt
        if self.y >= SCREEN_HEIGHT * 4 / 5 - self.r:
            if abs(self.vx) <= 5*SCALE and abs(self.vy) <= 5*SCALE:
                self.is_alive = False
            self.y = SCREEN_HEIGHT * 4 / 5 - self.r
            if self.vx >= 0:
                self.vx = max(0, self.vx - 0.2*self.vy)
            else:
                self.vx = min(0, self.vx + 0.2*self.vy)
            self.vy = -self.vy/2
        if not(0 - self.r < self.x < SCREEN_WIDTH + self.r):
            self.is_alive = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """
        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 15

    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Target.standard_radius
        self.color = COLORS[rnd.randint(0, len(COLORS) - 1)]
        self.is_alive = True

    def move(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        ax, ay = 0, 0
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += ax * dt
        self.vy += ay * dt
        if self.x >= SCREEN_WIDTH - self.r:
            self.x = SCREEN_WIDTH - self.r
            self.vx = -self.vx
        if self.x <= 0 + self.r:
            self.x = 0 + self.r
            self.vx = -self.vx
        if self.y >= SCREEN_HEIGHT*4/5 - self.r:
            self.y = SCREEN_HEIGHT*4/5 - self.r
            self.vy = -self.vy
        if self.y <= 0 + self.r:
            self.y = 0 + self.r
            self.vy = -self.vy

    def draw(self):
        """
        Draws a target
        :return:
        """
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """
        if other.detect_collision(self):
            self.is_alive = False

class Common_target(Target):
    def __init__(self, parent):
        super().__init__(RED)
        self.parent = parent

class Bomb:
    pass


def generate_random_targets(number: int):
    targets = []
    for i in range(number):
        x = rnd.randint(0, SCREEN_HEIGHT)
        y = rnd.randint(0, SCREEN_HEIGHT)
        v = rnd.randint(30, 60)
        angle = rnd.randint(0, 360)
        vx = v * math.cos(angle / (2 * math.pi))
        vy = v * math.sin(angle / (2 * math.pi))
        target = Target(x, y, vx, vy)
        targets.append(target)
    return targets


def movement(cannon, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if cannon.moving_dest == "NONE":
                cannon.moving_dest = "RIGHT"
            else:
                cannon.moving_dest = "NONE"
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if cannon.moving_dest == "NONE":
                cannon.moving_dest = "LEFT"
            else:
                cannon.moving_dest = "NONE"

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if cannon.moving_dest == "RIGHT":
                cannon.moving_dest = "NONE"
            else:
                cannon.moving_dest = "LEFT"
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if cannon.moving_dest == "LEFT":
                cannon.moving_dest = "NONE"
            else:
                cannon.moving_dest = "RIGHT"


def game_main_loop():
    targets = generate_random_targets(10)
    cannon = Cannon(SCREEN_WIDTH/2, SCREEN_HEIGHT*4/5)
    clock = pygame.time.Clock()
    projectiles = []
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cannon.on = True
            elif event.type == pygame.MOUSEBUTTONUP:
                cannon.on = False
                if cannon.shell_num > 0:
                    projectiles.append(cannon.fire())
                cannon.power = 0
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                movement(cannon, event)

        pygame.display.update()
        screen.fill(WHITE)
        # draw ground
        pygame.draw.polygon(screen, GRAY, (
            (0, SCREEN_HEIGHT * 4 / 5), (SCREEN_WIDTH, SCREEN_HEIGHT * 4 / 5), (SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, SCREEN_HEIGHT)), 0)
        cannon.move()
        cannon.aim(pygame.mouse.get_pos())
        cannon.draw()
        for target in targets:
            target.move(1 / FPS)
        for projectile in projectiles:
            projectile.move(1 / FPS)
            for target in targets:
                target.collide(projectile)
        for target in targets:
            target.draw()
            if not target.is_alive:
                targets.remove(target)
        for projectile in projectiles:
            projectile.draw()
            if not projectile.is_alive:
                projectiles.remove(projectile)
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.update()

    game_main_loop()
