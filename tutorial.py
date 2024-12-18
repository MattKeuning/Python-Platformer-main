import pygame
from sys import exit

pygame.init()
width = 800
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('8bit-pixel-art-night-sky-game-space-landscape-vector-50752838.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
    
    screen.blit(sky_surface,(0,0))

    pygame.display.update()
    clock.tick(60)

