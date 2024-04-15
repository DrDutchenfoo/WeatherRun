import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.surf = pygame.image.load("WeatherGull.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -7)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 7)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-8, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(8, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1300:
            self.rect.right = 1300
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 700:
            self.rect.bottom = 700


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Blaster2.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(1300 + 20, 1300 + 100),
                random.randint(0, 700),
            )
        )

        self.speed = random.randint(5, 15)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        size = random.randrange(50, 100)
        self.surf = pygame.Surface((size + random.randrange(20, 40), size))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(1300 + 20, 1300 + 100),
                random.randint(0, 700 + 100),
            )
        )

    def update(self):
        self.rect.move_ip(-6, 0)

        if self.rect.right < 0:
            self.kill()


class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super(Rain, self).__init__()
        size = random.randrange(2, 4)
        self.surf = pygame.Surface((size, size + random.randrange(4, 6)))
        self.surf.fill((70, 70, 150))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, 1400),
                random.randint(0, 0)
            )
        )

    def update(self):
        self.rect.move_ip(-1, 6)

        if self.rect.top > 700:
            self.kill()


class Thunder(pygame.sprite.Sprite):
    def __init__(self):
        super(Thunder, self).__init__()
        size = random.randrange(5, 15)
        self.surf = pygame.Surface((size, size + random.randrange(600, 800)))
        self.surf.fill((255, 240, 190))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, 1300),
                random.randint(-300, -300)
            )
        )

    def update(self):
        self.rect.move_ip(0, 30)

        if self.rect.top > 700:
            self.kill()
