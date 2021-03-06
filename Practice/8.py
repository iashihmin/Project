import pygame
import math
import random
from pygame.locals import *
from colors import *

#Класс для считывания изображения с компьютера для дальнейшего его
#использования в программе
class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(CAR)
        self.rect = self.image.get_rect()

pygame.init()
pygame.font.init()

#Функция для проверки того, что введенные пользователем данные удовлетворяют
#наложенным на них требованиям
def check(elem, v1, v2):
    if elem < v1 or elem > v2:
        return False
    else:
        return True
#Функция для проверки наличия в строке различных символов, помимо цифр
def digit(elem):
    return elem.isdigit()

mas = []

#Ввод данных пользователем
print("Данная программа представляет собой систему управления автомобилем на трассе. Просьба вводить все данные целыми числами.")
print("Введите начальную скорость автомобиля(от 0 до 100 км\ч):")
mas.append(input())
while digit(mas[-1]) == False:
    del mas[-1]
    print("Пожалуйста, используйте только цифры:")
    mas.append(input())
mas[-1] = float(mas[-1])
while check(mas[-1], 0, 100) != True:
    del mas[-1]
    print("Пожалуйста, введите начальную скорость от 0 до 100 км\ч:")
    mas.append(float(input()))
mas[-1] = math.trunc(mas[-1])
mas[-1] = int(mas[-1])

print("Введите приоритетную скорость автомобиля(от 80 до 100 км\ч):")
mas.append(input())
while digit(mas[-1]) == False:
    del mas[-1]
    print("Пожалуйста, используйте только цифры:")
    mas.append(input())
mas[-1] = float(mas[-1])
while check(mas[-1], 80, 100) != True:
    del mas[-1]
    print("Пожалуйста, введите приоритетную скорость от 80 до 100 км\ч:")
    mas.append(float(input()))
mas[-1] = math.trunc(mas[-1])
mas[-1] = int(mas[-1])

print("Введите мощность автомобиля(от 75 до 150 л.с.):")
mas.append(input())
while digit(mas[-1]) == False:
    del mas[-1]
    print("Пожалуйста, используйте только цифры:")
    mas.append(input())
mas[-1] = float(mas[-1])
while check(mas[-1], 75, 150) != True:
    del mas[-1]
    print("Пожалуйста, введите мощность автомобиля от 75 до 150 л.с.:")
    mas.append(float(input()))
mas[-1] = math.trunc(mas[-1])
mas[-1] = int(mas[-1])
initial = -int(mas[0])/2
priority = int(mas[1])
acceleration = (int(mas[2])-25)/1000

inf_spd = pygame.font.Font(None, 50)

#Загрузка изображения заднего фона и установка размеров экрана приложения
background = pygame.image.load('road.jpg')
background_size = background.get_size()
screen_width, screen_height = background_size
screen = pygame.display.set_mode([screen_width, screen_height])

#Ручной ввод начальных данных управляемого автомобиля и ботов
x_speed = 0
speed = [1, 1, initial]
x_coord = 235
y_coord = 580
x = 0
y = 0
y1 = -screen_height

by_spd = 0
bot_real_speed = -70
bx_crd = 235
by_crd = -199

by_spd1 = 0
bot_real_speed1 = -50
bx_crd1 = 45
by_crd1 = -199

#Функция, задающая систему управления, принимающая на вход скорости и координаты ботов и управляемого автомобиля, а
#на выход выдающая скорость управляемого автомобиля и поворот его руля
def double_overtaking(py_crd, by_crd, speed_of_convergence, b_spd, b1_spd, px_crd, py_spd, x_spd, by1_crd):
    a = 0
    mas = []
    l_spd = 0
    distance = py_crd - by_crd - 199  - 200
    distance1 = py_crd - by1_crd - 199
    distance2 = py_crd - by_crd - 199
    visibility = 580
    if distance2 < visibility:
            s_counts = math.fabs((py_spd - b_spd) / acceleration)
            f_counts = (distance / acceleration)
            if b_spd < b1_spd:
                if distance1 <= distance2:
                    if s_counts >= f_counts:
                        if py_spd*2 < b_spd:
                            py_spd = py_spd + acceleration
                        if py_spd*2 > b_spd:
                            py_spd = py_spd - acceleration
                    else:
                        if -py_spd*2 < priority:
                            py_spd = py_spd - acceleration
                        if -py_spd*2 > priority:
                            py_spd = py_spd + acceleration
                else:
                    c1 = (distance2 + 450)/(-(b_spd+priority*2)/30)
                    c2 = (distance1 - distance2 - 450)/(-(b1_spd+priority*2)/30)
                    if distance2 < 200:
                        if c1 > c2:
                            if px_crd > 45:
                                l_spd = x_spd
                                if -py_spd*2 < priority:
                                    py_spd = py_spd - acceleration
                                if -py_spd*2 > priority:
                                    py_spd = py_spd + acceleration

                        else:
                            s_counts = math.fabs((py_spd - b_spd) / acceleration)
                            f_counts = (distance / acceleration)
                            if s_counts >= f_counts:
                                if (px_crd >= 234 and px_crd <= 236) and by_crd < 800:
                                    if py_spd*2 < b_spd:
                                        py_spd = py_spd + acceleration
                                    if py_spd*2 > b_spd:
                                        py_spd = py_spd - acceleration
                    else:
                        if -py_spd*2 < priority:
                            py_spd = py_spd - acceleration
                        if -py_spd*2 > priority:
                            py_spd = py_spd + acceleration
                   
            if b_spd > b1_spd:
                if distance1 >= distance2:
                    s_counts = math.fabs((py_spd - b_spd) / acceleration)
                    f_counts = (distance / acceleration)
                    if s_counts >= f_counts:
                        if (px_crd >= 234 and px_crd <= 236) and by_crd < 800:
                            if py_spd*2 < b_spd:
                                py_spd = py_spd + acceleration
                            if py_spd*2 > b_spd:
                                py_spd = py_spd - acceleration
                            if py_spd*2 > b_spd-3 and py_spd*2 <= b_spd+1:
                                l_spd = x_spd
                        if px_crd >= 45 and px_crd < 235:
                            if px_crd >= 44 and px_crd <= 46:
                                if distance1 < 200:
                                    if py_spd*2 < b1_spd:
                                        py_spd = py_spd + acceleration  
                                    if py_spd*2 > b1_spd:
                                        py_spd = py_spd - acceleration
                                else:
                                    if -py_spd*2 < priority:
                                        py_spd = py_spd - acceleration
                                    if -py_spd*2 > priority:
                                        py_spd = py_spd + acceleration
                            else:
                                if distance1 >= 200:
                                    if -py_spd*2 < priority:
                                        py_spd = py_spd - acceleration
                                    if -py_spd*2 > priority:
                                        py_spd = py_spd + acceleration
                                if by1_crd < by_crd:
                                    l_spd = x_spd

                    else:
                        if distance2 < 200:
                            if py_spd*2 < b_spd:
                                py_spd = py_spd + acceleration
                            if py_spd*2 > b_spd:
                                py_spd = py_spd - acceleration
                        if -py_spd*2 < priority:
                            py_spd = py_spd - acceleration
                        if -py_spd*2 > priority:
                            py_spd = py_spd + acceleration
                else:
                    if px_crd < 235:
                        l_spd = -x_spd
                    s_counts = math.fabs((py_spd - b_spd) / acceleration)
                    f_counts = (distance / acceleration)
                    if s_counts >= f_counts:
                        if px_crd == 235:
                            if py_spd*2 < b_spd:
                                py_spd = py_spd + acceleration
                            if py_spd*2 > b_spd:
                                py_spd = py_spd - acceleration
                    if distance2 < 200:
                        if py_spd*2 < b_spd:
                            py_spd = py_spd + acceleration
                        if py_spd*2 > b_spd:
                            py_spd = py_spd - acceleration
    else:
        if px_crd < 235:
            l_spd = -x_spd
        if -py_spd*2 < priority:
            py_spd = py_spd - acceleration
        if -py_spd*2 > priority:
            py_spd = py_spd + acceleration
    mas.append(l_spd)
    mas.append(py_spd)
    return mas 

#Создание группы объектов, состоящих из автомобилей, для дальнейшего их изображения на экране
sprites = pygame.sprite.Group()
player = Block('car.png')
bot = Block('car2.png')
bot1 = Block('car2.png')
sprites.add(player)
sprites.add(bot)
sprites.add(bot1)

done = True
massiv = []
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

pygame.display.update()

#Цикл работы программы, в котором обновляются все данные и который отображает работу программы на экран
while done:
    a = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    end = -priority + 10
    start = end + 20

    #Выбор скорости автомобилей-ботов случайным образом
    if by_crd > 800:
        by_crd = random.uniform(-screen_height, -screen_height*(0.5))
        bot_real_speed = random.randint(end, start)
    if by_crd1 > 800:
        by_crd1 = random.uniform(-4*screen_height, -3*screen_height)
        bot_real_speed1 = random.randint(end, start)
        if bot_real_speed1 < (bot_real_speed + 5) and bot_real_speed1 > (bot_real_speed - 5):
            bot_real_speed1 = bot_real_speed-10
            if bot_real_speed1 < start:
               bot_real_speed1 = bot_real_speed + 10

    if bot_real_speed1 < (bot_real_speed + 5) and bot_real_speed1 > (bot_real_speed - 5):
        bot_real_speed1 = bot_real_speed-10
        if bot_real_speed1 < start:
            bot_real_speed1 = bot_real_speed + 10


    #Определение скорости поворота управляемого автомобиля в зависимости от скорости его движения
    if speed[-1] > -50:
        x_speed = -1
    else:
        x_speed = 50/speed[-1]

    #Подсчет скорости сближения управляемого автомобиля с автомобилями-ботами на экране
    by_spd = - (bot_real_speed - speed[-1]*2) / 30
    by_crd -= by_spd
    by_spd1 = - (bot_real_speed1 - speed[-1]*2) / 30
    by_crd1 -= by_spd1

    #Вызов функции, описывающей систему управления
    mas = double_overtaking(y_coord, by_crd, by_spd, bot_real_speed, bot_real_speed1, x_coord, speed[-1], x_speed, by_crd1)
    x_speed = mas[0]
    speed[-1] = mas[1]

    if speed[-1] > 0:
        speed[-1] = 0

    #Прокрутка заднего фона в зависимости от скорости движения управляемого автомобиля
    y1 -= speed[-1]/(1.4)
    y -= speed[-1]/(1.4)
    if y > screen_height:
        y = - screen_height
    if y1 > screen_height:
        y1 = - screen_height

    #Считывания координат задействованных в приложение объектов
    player.rect.x = x_coord
    player.rect.y = y_coord
    
    bot.rect.x = bx_crd
    bot.rect.y = by_crd

    bot1.rect.x = bx_crd1
    bot1.rect.y = by_crd1

    x_coord += x_speed

    if x_coord > 235 or x_coord < 45:
        x_speed = 0

    #Отображения всех объектов на экран приложения
    screen.blit(background, (x,y))
    screen.blit(background, (x,y1))
    sprites.draw(screen)
    screen.blit(inf_spd.render(str(int(round(-speed[-1]*2))) + 'км/ч', 1, WHITE), (200,5) )

    clock.tick(70)
    
    pygame.display.flip()
    pygame.display.update()

pygame.font.quit()
pygame.quit()
