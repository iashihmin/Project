import pygame
import time
from colors import *

class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

pygame.init()

screen_width = 400
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])

x_speed = 0
y_speed = 0

x_coord = 200
y_coord = 450

sprites = pygame.sprite.Group()
player = Block('car.jpg')
sprites.add(player)

done = True

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -5
                current_time = time.time()
            elif event.key == pygame.K_DOWN:
                y_speed = 5
            elif event.key == pygame.K_LEFT:
                x_speed = -1
            elif event.key == pygame.K_RIGHT:
                x_speed = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0

    player.rect.x = x_coord
    player.rect.y = y_coord
    
    x_coord += x_speed
    y_coord += y_speed

    screen.fill(WHITE)
          
    sprites.draw(screen)

    clock.tick(60)

    pygame.display.flip()


pygame.quit()
