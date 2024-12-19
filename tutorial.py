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
temp = pygame.image.load('snail2.png').convert_alpha()
player = pygame.image.load('clipart1361415.png').convert_alpha()
npx = 100
npy = 360
np = pygame.transform.scale(player, (60, 100))
player_rect = np.get_rect(topleft = (npx,npy))
snail_rect = enemy_surface1.get_rect(topleft = (700, 420))
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
        player_rect.y -= 10
        jump_count += 1
    if is_jump and jump_count >= 15:
        going_down = True

    if going_down:
        is_jump = False
        if player_rect.y == 360:
            going_down = False
            jump_count = 0
        player_rect.y += 5

        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 4
    if keys[pygame.K_LEFT]:
        player_rect.x -= 4
    
    

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    screen.blit(ground_surface,(400, 450))
    screen.blit(temp, snail_rect)
    screen.blit(text_surface,(300, 50))
    screen.blit(np, player_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    collision = player_rect.colliderect(snail_rect)
    if collision:
        pygame.quit()

    pygame.display.update()
    clock.tick(60)

