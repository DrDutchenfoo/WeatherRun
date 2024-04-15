import pygame
import random
import WeatherRunClasses
import WeatherRunAPI
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

WeatherRunAPI.get_location()
W = 0
if WeatherRunAPI.weather == "Clouds":
    W = 'c'
if WeatherRunAPI.weather == "Rain":
    W = 'r'
screenW = 1300
screenH = 700
counter = 0

pygame.init()
screen = pygame.display.set_mode((screenW, screenH))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 120)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 300)

ADDRAIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADDRAIN, 8)

ADDTHUN = pygame.USEREVENT + 4
pygame.time.set_timer(ADDTHUN, random.randrange(1000, 4000))

ADDCOUNTER = counter
pygame.time.set_timer(ADDCOUNTER, 1000)

player = WeatherRunClasses.Player(screenW / 3, screenH / 2)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
rain = pygame.sprite.Group()
thun = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDCOUNTER:
            counter = counter + 1
            print(counter)
        elif event.type == ADDENEMY:
            new_enemy = WeatherRunClasses.Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD and W == 'c':
            new_cloud = WeatherRunClasses.Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
        elif event.type == ADDRAIN and W == 'r':
            new_drop = WeatherRunClasses.Rain()
            rain.add(new_drop)
            all_sprites.add(new_drop)
        elif event.type == ADDTHUN and W == 'r':
            new_bolt = WeatherRunClasses.Thunder()
            thun.add(new_bolt)
            all_sprites.add(new_bolt)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    if W == 'c':
        clouds.update()
        screen.fill((150, 200, 255))
    elif W == 'r':
        rain.update()
        thun.update()
        screen.fill((100, 150, 200))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
    if pygame.sprite.spritecollideany(player, thun):
        player.kill()
        running = False

    pygame.display.flip()

    clock.tick(30)
