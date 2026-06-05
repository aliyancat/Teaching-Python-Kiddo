import pygame
import random
pygame.init()

health = 5

health_FONT = pygame.font.Font(None, 40)

health_x = 120
health_y = 120

health_decreaser_x = 100
health_decreaser_y = 200

health_width = 21
health_height = 67

WIDTH = 800
HEIGHT = 600

colour1 = random.randint(0,255)
colour2 = random.randint(0,255)
colour3 = random.randint(0,255)

x = 40
y = 20

#feel free to replace the numbers when ever you want.

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((colour1,colour2,colour3))
    keys = pygame.key.get_pressed()

    if keys [pygame.K_RIGHT]:
        if health_x < WIDTH - 21:
            health_x = health_x+0.1
    if keys [pygame.K_LEFT]:
        if health_x > 0:
            health_x = health_x-0.1
    if keys [pygame.K_DOWN]:
        if health_y < HEIGHT - 67:
            health_y = health_y+0.1
    if keys [pygame.K_UP]:
        if health_y > 0:
            health_y = health_y-0.1
    print (health_x, health_y)
    health_TEXT = health_FONT.render(f"health: {health}", True, (0, 0, 255))

    screen.blit(health_TEXT, (health_x, health_y))


    if keys [pygame.K_1]:
        health = health + 1

    if keys [pygame.K_c]:
        colour1 = random.randint(0,255)
        colour2 = random.randint(0,255)
        colour3 = random.randint(0,255)
        screen.fill((colour1,colour2,colour3)) 

    if keys [pygame.K_t]:
        x = random.randint(0,800)
        y = random.randint(0,600)

    if keys [pygame.K_2]:
        health = health - 1

    if health < 10:
        pygame.draw.rect(screen,(255,0,0),(x,y,health_width,health_height))
        health_width = 10
    if health > 10:
        pygame.draw.rect(screen,(0,255,0),(x,y,health_width,health_height))
        health_width = 50

    text_width = health_TEXT.get_width()
    text_height = health_TEXT.get_height()
    
    if (health_x < x + health_width and 
        health_x + text_width > x and
        health_y < y + health_height and
        health_y + text_height > y):
            print("TOO CLOSEE !!")

    text_width = health_TEXT.get_width()
    text_height = health_TEXT.get_height()
    
    if (health_x < health_decreaser_x + health_width and 
    health_x + text_width > health_decreaser_x and
    health_y < health_decreaser_y + health_height and
    health_y + text_height > health_decreaser_y):
        health = health - 1

    health_decreaser = pygame.draw.rect(screen,(245,67,21),(health_decreaser_x,health_decreaser_y,health_width,health_height))
   
    pygame.display.update()
pygame.quit()