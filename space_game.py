import pygame
import random



pygame.init()


width = 600
height = 400


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)


ship_width = 50
ship_height = 30



ship_x = width//2 - ship_width//2      # x location of the ship
ship_y = height - 60  # y location of the ship

ship_speed = 6

bullets = []
bullet_speed = 6


asteroids = []
asteroids_speed = 3 


score = 0

running = True

while running == True:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = ship_x + ship_width//2 
                bullet_y = ship_y
                current_bullet = (bullet_x, bullet_y)
                bullets.append(current_bullet)

                