import pygame
from colors import *

class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

pygame.init()


background = pygame.image.load('road.jpg')
background_size = background.get_size()
screen_width, screen_height = background_size
screen = pygame.display.set_mode([screen_width, screen_height])

x_speed = 0
y_speed = 0

x_coord = 200
y_coord = 450

x = 0
y = 0
y1 = -screen_height

sprites = pygame.sprite.Group()
player = Block('car.png')
sprites.add(player)

done = True

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


while done:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
            elif event.key == pygame.K_LEFT:
                x_speed = -2
            elif event.key == pygame.K_RIGHT:
                x_speed = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0
    y1 += 5
    y += 5
    screen.blit(background, (x,y))
    screen.blit(background, (x,y1))

    if y > screen_height:
        y = - screen_height
    if y1 > screen_height:
        y1 = - screen_height
        
    player.rect.x = x_coord
    player.rect.y = y_coord
    
    x_coord += x_speed
    y_coord += y_speed
          
    sprites.draw(screen)

    clock.tick(60)

    pygame.display.flip()
    pygame.display.update()


pygame.quit()
