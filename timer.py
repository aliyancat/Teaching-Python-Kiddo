import pygame
import time


pygame.init()


screen = pygame.display.set_mode((800,600))

font = pygame.font.SysFont(None, 50)


start_time = 10

running = True

while running:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed = pygame.time.get_ticks() // 1000

    time_left = start_time - elapsed

    if time_left <= 0:
        time_left = 0

    text = font.render(f"Time Left: {time_left}", True, (255,255,255))

    screen.fill((0,0,0))
    screen.blit(text, (250,250))
    pygame.display.update()

pygame.quit()