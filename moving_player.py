import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

x = 40
y = 20
box_width = 21

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((1,2,3))

    if x < WIDTH - box_width:
        x = x + 0.1

    pygame.draw.rect(screen,(255,153,0),(x,y,21,67))

    pygame.display.update()

pygame.quit()