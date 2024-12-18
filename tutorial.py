import pygame
from sys import exit

pygame.init()
width = 800
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('8bit-pixel-art-night-sky-game-space-landscape-vector-50752838.jpg')
ground_surface = pygame.image.load('stone.png')
text_surface = test_font.render('Matt\'s Mario', False, 'Grey')
enemy_surface1 = pygame.image.load('snail1.png')
enemy_surface1 = pygame.image.load('snail1.png')
snail_x_pos = 700
temp = pygame.image.load('snail2.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    screen.blit(ground_surface,(400, 450))
    screen.blit(temp, (snail_x_pos, 420))
    screen.blit(text_surface,(300, 50))
    snail_x_pos -= 5
    if snail_x_pos % 2 == 0:
        temp = pygame.image.load('snail1.png')
    else:
        temp = pygame.image.load('snail2.png')
    if snail_x_pos < -100: snail_x_pos = 800
    


    pygame.display.update()
    clock.tick(60)

