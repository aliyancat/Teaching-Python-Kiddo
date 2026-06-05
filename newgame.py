import pygame
import random
pygame.init()

pygame.mixer.init()
landing = pygame.mixer.Sound("bouncy.mp3")

WIDTH = 800
HEIGHT = 600


 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Platformer Game")

font = pygame.font.SysFont(None, 36)    


clock = pygame.time.Clock()

player_x = 400
player_y = 200
player_size = 40
speed = 5

was_on_ground = False

gravity = 0.5
velocity_y = 0 # if positive, that means moving down
               # if negative, that means moving up
jump_force = -22 # by the power it jumps up
on_ground = False

platform_x = 0
platform_y = 500
platform_width = 800
platform_height = 50

coin_size = 20 
coin_x = random.randint(0 , WIDTH - coin_size ) 
coin_y = random.randint(0 , platform_y - coin_size )

score = 0



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_force
                on_ground = False
                

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    velocity_y += gravity    
    player_y += velocity_y


    #doing this so the player can stand
    #on the platform and doesnt fall through it
    if player_y + player_size >= platform_y:

        if not was_on_ground:
            landing.play()
        player_y = platform_y - player_size
        velocity_y = 0
        on_ground = True
        
    if player_x < coin_x + coin_size and player_x + player_size > coin_x and player_y < coin_y + coin_size and player_y + player_size > coin_y:
        score += 1
        
        if score >= 2:
            print("You win!")   
            running = False

        coin_x = random.randint(0, WIDTH - coin_size)
        coin_y = random.randint(0, platform_y - coin_size)


    screen.fill((30,30,30))


    pygame.draw.circle(screen,(243,199,13),(coin_x,coin_y),coin_size)

    pygame.draw.rect(screen,(100,200,100),(platform_x,platform_y,platform_width,platform_height))
    pygame.draw.rect(screen,(200,50,50),(player_x,player_y,player_size,player_size))

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10,10))

    pygame.display.update()
    clock.tick(60)
    was_on_ground = on_ground


pygame.quit()