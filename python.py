import pygame

# --------------------
# SETUP
# --------------------
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WASD Animation Game")

clock = pygame.time.Clock()

# --------------------
# PLAYER SETTINGS
# --------------------
x, y = 225, 225
speed = 5

# Load animation frames
walk_frames = [
    pygame.image.load("walk1.png"),
    pygame.image.load("walk2.png"),
    pygame.image.load("walk3.png")
]

# Resize frames (optional but recommended)
walk_frames = [pygame.transform.scale(img, (50, 50)) for img in walk_frames]

frame_index = 0

# --------------------
# GAME LOOP
# --------------------
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    # --------------------
    # MOVEMENT (WASD)
    # --------------------
    if keys[pygame.K_w]:
        y -= speed
        moving = True
    if keys[pygame.K_s]:
        y += speed
        moving = True
    if keys[pygame.K_a]:
        x -= speed
        moving = True
    if keys[pygame.K_d]:
        x += speed
        moving = True

    # Keep player on screen
    x = max(0, min(x, WIDTH - 50))
    y = max(0, min(y, HEIGHT - 50))

    # --------------------
    # ANIMATION
    # --------------------
    if moving:
        frame_index += 0.2
        if frame_index >= len(walk_frames):
            frame_index = 0
    else:
        frame_index = 0  # idle frame

    # --------------------
    # DRAW
    # --------------------
    screen.fill((255, 255, 255))  # white background
    screen.blit(walk_frames[int(frame_index)], (x, y))
    pygame.display.update()

pygame.quit()
