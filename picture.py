import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))

dark_gray = (119, 136, 153)
light_gray = (220, 220, 220)
black = (0, 0, 0)
yellow = (255, 255, 0)
brown = (139, 69, 19)
green = (128, 128, 0)
balkon = (96,96,96)
def full_picture():
    rect(screen, dark_gray, (0,0, 794,500))  # небо

    def home (x_home , y_home, width_home, height_home):
        """

        :param x_home: середины дома
        :param y_home: середины дома
        :param width_home: ширина только стен, без крыши и балкона
        :param height_home:  без учета крыши и  труб(трубы вообще отдельной
        функцией пойдут)
        """
        rect(screen, green,(x_home - width_home/2, y_home - height_home, width_home, height_home)) # кирпичи

        polygon(screen, black, [(x_home - width_home/1.6, y_home - height_home), (x_home + width_home/1.6, y_home - height_home),    # крыша
                                (x_home + width_home/2.2, y_home - height_home * 1.05), (x_home - width_home/2.2, y_home - height_home * 1.05)])
        #верхние окна, их 4, ширина каждого width_home/8 => ширина проемов(их 5) width_home/10

        glass_width = width_home/8

        proem_width = width_home/10

        for i in range(4):
            x = x_home - width_home/2 + i * glass_width + (i + 1) * proem_width
            rect(screen, light_gray, (x, y_home - height_home, glass_width, height_home/2.7))

    home(794/2,1123/2,100,300) # тест



full_picture()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()