import random as rnd
import math
import pygame

FPS = 60
GRAVITY_ACCELERATION = 9.8  # Ускорение свободного падения для снаряда.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
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
    min_v = 25
    length = 100
    height = 10

    def __init__(self, x, y):
        self.power = 0
        self.on = False
        self.x = x
        self.y = y
        self.shell_num = 5
        self.direction = math.pi / 4
        self.color = WHITE

    def aim(self, pos):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param pos: tuple (x, y) of mouse coords
        :return: None
        """
        x = pos[0] - self.x
        y = self.y - pos[1]
        if x != 0:
            self.direction = math.atan(y / x)
        else:
            self.direction = math.pi / 2
        if self.on:
            self.power += Cannon.max_power / FPS
        if self.power > Cannon.max_power:
            self.power = Cannon.max_power

    def fire(self, ):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """
        if self.shell_num > 0:
            self.shell_num -= 1
            length = Cannon.length
            x, y = (self.x + length * math.cos(self.direction), self.y - length * math.sin(self.direction))
            vx = Cannon.min_v * (self.power + 1) * math.cos(self.direction)
            vy = Cannon.min_v * (self.power + 1) * math.sin(self.direction)
            projectile = Shell(x, y, vx, -vy)
            return projectile

    def draw(self):
        """
        Draws a cannon and increases power if cannon is on
        :return:
        """
        color = (255, (Cannon.max_power - self.power) * 255 / Cannon.max_power, (Cannon.max_power - self.power) * 255 / Cannon.max_power)
        half = Cannon.height / 2
        length = Cannon.length
        pos1 = (self.x - half * math.sin(self.direction), self.y - half * math.cos(self.direction))
        pos2 = (self.x - half * math.sin(self.direction) + length * math.cos(self.direction),
                self.y - half * math.cos(self.direction) - length * math.sin(self.direction))
        pos3 = (self.x + half * math.sin(self.direction) + length * math.cos(self.direction),
                self.y + half * math.cos(self.direction) - length * math.sin(self.direction))
        pos4 = (self.x + half * math.sin(self.direction), self.y + 10 * math.cos(self.direction))
        pygame.draw.polygon(screen, color, [pos1, pos2, pos3, pos4])


class Shell:
    standard_radius = 25

    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Shell.standard_radius
        self.deleted = False

    def move(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        dt = 15 / FPS
        ax, ay = 0, GRAVITY_ACCELERATION
        self.x += self.vx * dt + ax * (dt ** 2) / 2
        self.y += self.vy * dt + ay * (dt ** 2) / 2
        self.vx += ax * dt
        self.vy += ay * dt
        if not (self.x in (0 + self.r, SCREEN_WIDTH - self.r) and self.y in (0 + self.r, SCREEN_HEIGHT - self.r)):
            self.deleted = True

    def draw(self):
        pygame.draw.circle(screen, RED, (int(round(self.x)), int(round(self.y))), self.r)

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
        if self.y >= SCREEN_HEIGHT - self.r:
            self.y = SCREEN_HEIGHT - self.r
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
        pass  # TODO


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


def game_main_loop():
    targets = generate_random_targets(10)
    cannon = Cannon(0, 500)
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
        pygame.display.update()
        screen.fill(BLACK)
        cannon.aim(pygame.mouse.get_pos())
        cannon.draw()
        for target in targets:
            target.move(1 / FPS)

        for target in targets:
            target.draw()

        for projectile in projectiles:
            projectile.move(1 / FPS)
        for projectile in projectiles:
            projectile.draw()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.update()

    game_main_loop()
