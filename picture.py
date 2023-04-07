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

def full_picture():
    rect(screen, dark_gray, (0,0, 794,500))  # небо

    def home():
        pass



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