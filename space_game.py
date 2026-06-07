import pygame
import random

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

ship_width = 50
ship_height = 30

ship_x = width // 2 - ship_width // 2
ship_y = height - 60

ship_speed = 6

bullets = []
bullet_speed = 6

asteroids = []
asteroids_speed = 3

score = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = ship_x + ship_width // 2
                bullet_y = ship_y
                bullets.append([bullet_x, bullet_y])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed

    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed

    if ship_x < 0:
        ship_x = 0

    if ship_x > width - ship_width:
        ship_x = width - ship_width

    if random.randint(1, 40) == 1:
        asteroid_x = random.randint(0, width - 40)
        asteroid_y = 0
        asteroids.append([asteroid_x, asteroid_y])

    for bullet in bullets:
        bullet[1] -= bullet_speed

    new_bullets = []
    for bullet in bullets:
        if bullet[1] > 0:
            new_bullets.append(bullet)

    bullets = new_bullets

    for asteroid in asteroids:
        asteroid[1] += asteroids_speed

    new_asteroids = []
    for asteroid in asteroids:
        if asteroid[1] < height:
            new_asteroids.append(asteroid)

    asteroids = new_asteroids

    for bullet in bullets[:]:
        for asteroid in asteroids[:]:

            bullet_x = bullet[0]
            bullet_y = bullet[1]

            asteroid_x = asteroid[0]
            asteroid_y = asteroid[1]

            if (bullet_x > asteroid_x and bullet_x < asteroid_x + 40 and
                bullet_y > asteroid_y and bullet_y < asteroid_y + 40):

                score += 1

                if bullet in bullets:
                    bullets.remove(bullet)

                if asteroid in asteroids:
                    asteroids.remove(asteroid)

                break

    for asteroid in asteroids:

        asteroid_x = asteroid[0]
        asteroid_y = asteroid[1]

        if (ship_x < asteroid_x + 40 and
            ship_x + ship_width > asteroid_x and
            ship_y < asteroid_y + 40 and
            ship_y + ship_height > asteroid_y):

            running = False

    screen.fill((0, 0, 0))

    pygame.draw.polygon(
        screen,
        (0, 255, 0),
        [
            (ship_x, ship_y + ship_height),
            (ship_x + ship_width // 2, ship_y),
            (ship_x + ship_width, ship_y + ship_height)
        ]
    )

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), (bullet[0], bullet[1], 5, 12))

    for asteroid in asteroids:
        pygame.draw.circle(
            screen,
            (128, 128, 128),
            (asteroid[0] + 20, asteroid[1] + 20),
            20
        )

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

screen.fill((0, 0, 0))

game_over_font = pygame.font.SysFont(None, 90)

game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
final_score = font.render("Final Score: " + str(score), True, (255, 255, 255))

screen.blit(game_over_text, (140, 140))
screen.blit(final_score, (180, 220))

pygame.display.update()
pygame.time.delay(3000)

pygame.quit()