import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

running = True

while running:


 for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 screen.fill((255,255,0))


 pygame.draw.rect(screen, (255,255,255),(100,100,50,50))
 pygame.draw.circle(screen, (255,0,0), (200,200), 30)

 pygame.display.update()
pygame.quit()