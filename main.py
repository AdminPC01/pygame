import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((300, 300))


clock = pygame.time.Clock()
clock.tick(FPS)

rect(screen, (10, 100, 50), (100, 10, 190, 10))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


