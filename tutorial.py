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
ground_surface = pygame.image.load('stone.png').convert()
text_surface = test_font.render('Matt\'s Mario', False, 'Grey')
enemy_surface1 = pygame.image.load('snail1.png').convert_alpha()
snail_x_pos = 700
temp = pygame.image.load('snail2.png').convert_alpha()
player = pygame.image.load('clipart1361415.png')
np = pygame.transform.scale(player, (60, 100))
npx = 100
npy = 360
jump_count = 0
is_jump = False
going_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if is_jump:
                    break
                else:
                    is_jump = True

    if is_jump and jump_count < 15:
        npy -= 10
        jump_count += 1
    if is_jump and jump_count >= 15:
        going_down = True

    if going_down:
        is_jump = False
        if npy == 360:
            going_down = False
            jump_count = 0
        npy += 5

        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        npx += 4
    if keys[pygame.K_LEFT]:
        npx -= 4
    
    

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    screen.blit(ground_surface,(400, 450))
    screen.blit(temp, (snail_x_pos, 420))
    screen.blit(text_surface,(300, 50))
    screen.blit(np,(npx,npy))
    snail_x_pos -= 5
    if snail_x_pos % 2 == 0:
        temp = pygame.image.load('snail1.png')
    else:
        temp = pygame.image.load('snail2.png')
    if snail_x_pos < -100:
        snail_x_pos = 800

    pygame.display.update()
    clock.tick(60)

