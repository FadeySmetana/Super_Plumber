import pygame
from main import *
 
pygame.init()
 
sc = pygame.display.set_mode((300, 200))
 
pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75))
pygame.draw.rect(sc, (64, 128, 255), (150, 20, 100, 75), 8)# здесь будут рисоваться фигуры
 
pygame.display.update()
 
while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                main()