import pygame
import random
pygame.init()


width = 800
height = 600 

screen = pygame.display.set_mode((width,height))


x = random.randint(50,750)
y = random.randint(50,550)

size = 30

score = 0

font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


move_delay = 1000 # 1 second
last_move_time = pygame.time.get_ticks() #gives the current time in milliseconds


running = True

while running:
    screen.fill((0,0,0))

    current_time = pygame.time.get_ticks()
    duration = current_time - last_move_time

    if duration >= move_delay: 
        x = random.randint(50,750)
        y = random.randint(50,550)
        last_move_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = event.pos

            distance = ((mouse_x - x)**2 + (mouse_y - y)**2)**0.5

            if distance <= size:
                score +=1 

                x = random.randint(50,750)
                y = random.randint(50,550)
                last_move_time = pygame.time.get_ticks()
                
    pygame.draw.circle(screen,(255,0,0),(x,y),size)     
    score_text = font.render(f'Score: {score}', True, (255,255,255))
    screen.blit(score_text, (10,10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()



 

        


 