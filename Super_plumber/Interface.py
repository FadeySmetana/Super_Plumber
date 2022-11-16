import pygame
from pygame import *

pygame.init()


class Interface:
    def __init__(self):
        self.running = True
        self.pause_text = pygame.font.SysFont('Consolas', 72).render('Pause', True, pygame.color.Color('White'))
        self.choose = 0  # Изначально не выбран номер уровня
        self.reg_or_sign = 0  # Изначально не выбрано действие
        myrecord = 0
        login = ''
        self.login = ''

    def MainMenu(self):
        sc = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Super_Plumber BETA")

        logo = pygame.image.load('%s/PAC-MAN_Logo.png')
        logo_rect = logo.get_rect(bottomright=(800, 220))
        sc.blit(logo, logo_rect)

        START = pygame.draw.rect(sc, (255, 255, 255), (300, 280, 200, 40),
                                 1)  # отступ_слева    отступ_сверху    длинна    высота
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('START', 1, (255, 255, 255))
        sc.blit(text1, (361, 290))

        EXIT = pygame.draw.rect(sc, (255, 255, 255), (300, 330, 200, 40),
                                1)  # отступ_слева    отступ_сверху    длинна    высота
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('EXIT', 1, (255, 255, 255))
        sc.blit(text2, (370, 340))

        f3 = pygame.font.Font(None, 18)
        text3 = f3.render('by Fs', 1, (255, 255, 255))
        sc.blit(text3, (2, 620))

        f4 = pygame.font.Font(None, 18)
        text4 = f4.render('v 1.0', 1, (255, 255, 255))
        sc.blit(text4, (386, 620))

        pygame.display.update()
        while 1:
            pygame.time.delay(1)
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    click = START.collidepoint(pygame.mouse.get_pos())
                    clickE = EXIT.collidepoint(pygame.mouse.get_pos())
                    if clickE == 1:
                        exit()
                    if click == 1:
                        print('Игра началась!!!')
                        return

    def EndGame(self):
        sc = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Super_Plumber BETA")

        Restart = pygame.draw.rect(sc, (255, 255, 255), (300, 280, 200, 40),
                                   1)  # отступ_слева    отступ_сверху    длинна    высота
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('RESTART', 1, (255, 255, 255))
        sc.blit(text1, (344, 290))

        EXIT = pygame.draw.rect(sc, (255, 255, 255), (300, 330, 200, 40),
                                1)  # отступ_слева    отступ_сверху    длинна    высота
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('EXIT', 1, (255, 255, 255))
        sc.blit(text2, (370, 340))

        pygame.display.update()
        while 1:
            pygame.time.delay(1)
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    click = Restart.collidepoint(pygame.mouse.get_pos())
                    clickE = EXIT.collidepoint(pygame.mouse.get_pos())
                    if clickE == 1:
                        exit()
                    if click == 1:
                        self.MainMenu()
                        return

    def WinGame(self):
        sc = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Super_Plumber BETA")

        Restart = pygame.draw.rect(sc, (255, 255, 255), (300, 280, 200, 40),
                                   1)  # отступ_слева    отступ_сверху    длинна    высота
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('RESTART', 1, (255, 255, 255))
        sc.blit(text1, (344, 290))

        EXIT = pygame.draw.rect(sc, (255, 255, 255), (300, 330, 200, 40),
                                1)  # отступ_слева    отступ_сверху    длинна    высота
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('EXIT', 1, (255, 255, 255))
        sc.blit(text2, (370, 340))

        WINNER = Restart = pygame.draw.rect(sc, (0, 0, 255), (0, 0, 800, 220))
        f3 = pygame.font.Font(None, 110)
        text3 = f3.render('WINNER', 1, (255, 255, 255))
        sc.blit(text3, (247.5, 80))

        pygame.display.update()
        while 1:
            pygame.time.delay(1)
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    click = Restart.collidepoint(pygame.mouse.get_pos())
                    clickE = EXIT.collidepoint(pygame.mouse.get_pos())
                    if clickE == 1:
                        exit()
                    if click == 1:
                        self.MainMenu()
                        break