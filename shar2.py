import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50
screen = pygame.display.set_mode((900, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
color = COLORS[randint(0, 5)]

newball_list = []

for i in range(15):

    x = randint(100, 700)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    dx = randint(4, 8)
    dy = randint(3, 7)
    
    circle(screen, color, (x, y), r)

    newball_list.append([color, x, y, r, dx, dy])

clock = pygame.time.Clock()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

p = 0 
q = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 20)
                pygame.display.update()
    screen.fill(BLACK)

#процесс для каждого шарика
    for i in range(len(newball_list)):
        color = newball_list[i][0]
        x = newball_list[i][1]
        y = newball_list[i][2] 
        r = newball_list[i][3]
        dx= newball_list[i][4]
        dy= newball_list[i][5]
# Нарисовать шарик
        pygame.draw,circle(screen, color, (x,y), r)

# Передвинуть исходную точку шарик
        newball_list[i][1] += dx
        newball_list[i][2] += dy

# Заставить шарик отпрыгнуть, если нужно
        if newball_list[i][1] + newball_list[i][3]> 900 or newball_list[i][1] - newball_list[i][3]< 0:
            newball_list[i][4] = newball_list[i][4] * -1
        if newball_list[i][2] + newball_list[i][3] > 900 or newball_list[i][2] - newball_list[i][3]< 0:
            newball_list[i][5] = newball_list[i][5] * -1
# Заставить шарики отскакивать друг от друга
        for j in range(len(newball_list)):
            if j != i:

                if (newball_list[i][1] - newball_list[j][1])^2 + (newball_list[i][2] - newball_list[j][2])^2 == (newball_list[i][3] + newball_list[j][3])^2:

                    newball_list[j][4] = newball_list[j][4] * -1 
                    newball_list[i][4] = newball_list[i][4] * -1
                    newball_list[j][5] = newball_list[j][5] * -1
                    newball_list[i][5] = newball_list[i][5] * -1

    pygame.display.flip()

#подсчет очков

    if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x0 = event.pos[0]
        y0 = event.pos[1]
        d = 40
        if (x0 >= (x - d) and x0 <= (x + d)) and  (y0 >= (y - d) and y0 <= (y + d)) and r<= 50:
            p += 2
        elif (x0 >= (x - d) and x0 <= (x + d)) and  (y0 >= (y - d) and y0 <= (y + d)) and r>= 50:          
            q += 1
        else: 
            k = 0 

        score = q + p
        print(score)


clock.tick(20)          

pygame.quit()