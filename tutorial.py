import pygame


pygame.init()
width = 800
height = 500
screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # draw elements
    # update everything
    pygame.display.update()


