import pygame
from pygame.locals import *
from colors import *

class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(CAR)
        self.rect = self.image.get_rect()

pygame.init()
pygame.font.init()


''' input_priority_speed '''
def key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def draw(screen, speed):
    font = pygame.font.Font(None,40)
    screen.blit(font.render(speed, 1, WHITE),(0, (screen.get_height()/2)))
    pygame.display.flip()

def spd(screen, speed):
    mas_of_digits = []
    draw(screen, speed + ": " )
    while 1:
        inkey = key()
        if inkey == K_RETURN:
            if len(mas_of_digits)!=0:
                break
        elif inkey <= 57 and inkey >= 48 or inkey == 44:
            mas_of_digits.append(chr(inkey))
        answer = ''.join(map(str, mas_of_digits))
        draw(screen, speed + ': ' + answer)
    return mas_of_digits
screen = pygame.display.set_mode((900,50))
mas = (''.join(map(str, spd(screen, 'Priority speed(km/h),Acceleration')))).split(',')
priority = int(mas[0])

acceleration = (int(mas[1])-25)/1000
#print(acceleration)
''' --- '''


inf_spd = pygame.font.Font(None, 50)

background = pygame.image.load('road.jpg')
background_size = background.get_size()
screen_width, screen_height = background_size
screen = pygame.display.set_mode([screen_width, screen_height])

#info = pygame.Surface( (150, 50 ))

''' player '''
x_speed = 0
speed = [0, 0, 0]
x_coord = 235
y_coord = 580
x = 0
y = 0
y1 = -screen_height
''' --- '''
''' bot '''
by_spd = 0
bot_real_speed = -60
bx_crd = 235
by_crd = 300
''' --- '''

sprites = pygame.sprite.Group()
player = Block('car.png')
prect = pygame.image.load('car.png').convert().get_rect()
bot = Block('car2.png')
#print(pygame.image.load('car.png').get_size())
brect = pygame.image.load('car2.png').convert().get_rect()
sprites.add(player)
sprites.add(bot)

done = True


clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


pygame.display.update()
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
        if event.type == pygame.KEYDOWN:
            '''
            if event.key == pygame.K_UP:
                speed.append(speed[-1]-1)
                y_speed = speed[-1]
                del speed[0]
                
            elif event.key == pygame.K_DOWN:
                speed.append(speed[-1]+1)
                del speed[0]'''
                
            if event.key == pygame.K_LEFT:
                if speed[-1] != 0:
                    if x_coord > 10:
                        if speed[-1] > -50:
                            x_speed = -2
                        else:
                            x_speed = 100/speed[-1]

            elif event.key == pygame.K_RIGHT:
                if speed[-1] != 0:
                    if x_coord < 275:
                        if speed[-1] > -50:
                            x_speed = 2
                        else:
                            x_speed = - 100/speed[-1]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0

    

        
    '''player and bot'''
    if (by_crd+199) > (y_coord - 80) and bx_crd < (x_coord + 180) and by_crd < 800 and x_coord > 50:
        if x_coord > 10:
            if speed[-1] > -50:
                x_speed = -2
            else:
                x_speed = 100/speed[-1]
    elif bx_crd > (x_coord+180) and (by_crd+199) > (y_coord - 80):
        if speed[-1] != 0:
            if x_coord < 275:
                if speed[-1] > -50:
                    x_speed = 2
                else:
                    x_speed = - 100/speed[-1]        

        #speed[-1] += ((by_crd+199)-(y_coord-80))/(-speed[-1]+2)

        
    if speed[-1] > 0:
        speed[-1] = 0
        
    else:
        if -speed[-1]*2 < priority:
            speed[-1] = speed[-1] - acceleration
            #print(speed[-1])
    '''---'''

    '''bot speed'''
    by_spd = - (bot_real_speed - speed[-1]*2) / 30
    by_crd -= by_spd
    '''---'''

    y1 -= speed[-1]
    y -= speed[-1]

    if by_crd > screen_height:
        by_crd = - screen_height
    if y > screen_height:
        y = - screen_height
    if y1 > screen_height:
        y1 = - screen_height

    
    

    player.rect.x = x_coord
    player.rect.y = y_coord
    

    bot.rect.x = bx_crd
    bot.rect.y = by_crd

    x_coord += x_speed

    if x_coord > 235 or x_coord < 45:
        x_speed = 0

          
    
    screen.blit(background, (x,y))
    screen.blit(background, (x,y1))
    #screen.blit(info, (250,0) )
    sprites.draw(screen)
    screen.blit(inf_spd.render(str(int(-speed[-1]*2)) + 'km/h', 1, WHITE), (200,5) )

    clock.tick(60)

    pygame.display.flip()
    pygame.display.update()

pygame.font.quit()
pygame.quit()
