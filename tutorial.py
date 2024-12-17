import pygame
from sys import exit

pygame.init()
width = 800
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner Game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw elements
    # update everything
    pygame.display.update()


