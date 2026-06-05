import pygame
import random

pygame.init()
pygame.mixer.init()

die_s = pygame.mixer.Sound("bounce.mp3")
eat_s = pygame.mixer.Sound("eating.mp3")

game_b = pygame.image.load("snake_bg.png")

with open("hi_score.txt","r") as file:
    high_score = int(file.read())

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_block = 20
snake_speed = 10

level = 1

snake_x = 100
snake_y = 100

snake = [(snake_x, snake_y)]
direction = "right"

score = 0

font = pygame.font.SysFont(None, 35)
fontd = pygame.font.SysFont(None, 100)

food_x = random.randrange(0, width, snake_block)
food_y = random.randrange(0, height, snake_block)
food_type = random.choice(["red", "green", "gold"])

died_text = fontd.render("u died", True, (255, 0, 0))

running = True
clock = pygame.time.Clock()

while running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        clock.tick(snake_speed*1.5)

    else:
        clock.tick(snake_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if keys[pygame.K_LEFT] and direction != "right":
        direction = "left"

    if keys[pygame.K_RIGHT] and direction != "left":
        direction = "right"

    if keys[pygame.K_UP] and direction != "down":
        direction = "up"

    if keys[pygame.K_DOWN] and direction != "up":
        direction = "down"

    if direction == "left":
        snake_x -= snake_block

    if direction == "right":
        snake_x += snake_block

    if direction == "up":
        snake_y -= snake_block

    if direction == "down":
        snake_y += snake_block

    new_head = (snake_x, snake_y)
    snake.insert(0, new_head)

    if snake_x == food_x and snake_y == food_y:

        if food_type == "red":
            score += 1
        elif food_type == "green":
            score += 5
        elif food_type == "gold":
            score += 10

        if score > high_score:
            high_score = score

        while True:
            food_x = random.randrange(0, width, snake_block)
            food_y = random.randrange(0, height, snake_block)
            if (food_x, food_y) not in snake:
                break

        food_type = random.choice(["red", "green", "gold"])

        eat_s.play()

    else:
        snake.pop()

    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        running = False

    if new_head in snake[1:]:
        running = False

    screen.blit(game_b,(0,0))

    if food_type == "red":
        color = (255,0,0)
    elif food_type == "green":
        color = (0,255,0)
    else:
        color = (255,215,0)

    pygame.draw.rect(screen, color, (food_x, food_y, snake_block, snake_block))

    for part in snake:
        pygame.draw.rect(screen, (0,255,0), (part[0], part[1], snake_block, snake_block))

    level = score // 20 + 1

    snake_speed = 10 + level


    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, [10,10])

    score1_text = font.render("HIGHSCORE: " + str(high_score), True, (255,255,255))
    screen.blit(score1_text, [10,30])

    level_text = font.render("Level: " + str(level), True, (255,255,255))
    screen.blit(level_text, [10,50])

    pygame.display.update()

screen.fill((0,0,0))
screen.blit(died_text, [200,150])
die_s.play()
pygame.display.update()
pygame.time.delay(3000)

with open("hi_score.txt","w") as file:
    file.write(str(high_score))

pygame.quit()