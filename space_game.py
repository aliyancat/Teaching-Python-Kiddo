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


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed

    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed


    if ship_x < 0:  # keep it inside the screen
        ship_x = 0

    if ship_x > width - ship_width:
        ship_x = width - ship_width

    # spawning the enemies #

    if random.randint(1,40) == 1: 
        asteroid_x = random.randint(0,width-40)
        asteroid_y = 0 or -10

        current_asteroid = (asteroid_x, asteroid_y) 
        asteroids.append(current_asteroid)
        
    # moving the bullets #

    for every_bullet in bullets:
        every_bullet[1] = every_bullet[1] - bullet_speed


    #removing the bullets that left the screen #

    active_bullets = []

    for every_bullet in bullets:
        if every_bullet[1] > 0:
            active_bullets.append(every_bullet)

    bullets = active_bullets


    # interaction between asteroids n bullets #

    for every_bullet in bullets:
        for every_asteroid in asteroids:
            
            bullet_x = every_bullet[0]
            bullet_y = every_bullet[1]

            asteroid_x = every_asteroid[0]
            asteroid_y = every_asteroid[1]

            if (bullet_x > asteroid_x and bullet_x < asteroid_x + 40) and (bullet_y > asteroid_y and bullet_y < asteroid_y + 40):
                score += 1

                bullets.remove(every_bullet)
                asteroids.remove(every_asteroid)

                break

    # interaction between the asteroid and the sapceship #

    for every_asteroid in asteroids:
        asteroid_x = every_asteroid[0]
        asteroid_y = every_asteroid[1]

        if (ship_x < asteroid_x + 40 and ship_x + ship_width > asteroid_x) and (ship_y < asteroid_y + 40 and ship_y + ship_height > asteroid_y):
            
            running = False


    screen.fill((0,0,0))
    pygame.draw.polygon(screen, (0,255,0), ((ship_x, ship_y + ship_height), (ship_x + ship_width//2, ship_y), (ship_x + ship_width, ship_y + ship_height)))

    
    for every_bullet in bullets:
        pygame.draw.rect(screen, (255,0,0), (every_bullet[0], every_bullet[1], 5, 12))

    

    for every_asteroid in asteroids:
        pygame.draw.circle(screen, (128,128,128), (every_asteroid[0]+20, every_asteroid[1]+20), 20)




    


    







    



                