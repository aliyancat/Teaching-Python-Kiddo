import pygame

pygame.init()

width = 300
height = 300
screen = pygame.display.set_mode((width, height))


board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

player = "X"
running = True

font = pygame.font.Font(None, 100)

winner = None
game_over = False
small_font = pygame.font.Font(None,40)

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    
    if board[2][0] == board[1][1] == board[0][2] != "":
        return board[0][2]
    
    return None

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            row = y // 100   
            col = x // 100   

            if board[row][col] == "" and not game_over:
                board[row][col] = player

                winner = check_winner()
                
                if winner:
                    game_over = True

                if player == "X":
                    player = "O"
                elif player == "O":
                    player = "X"

    screen.fill((255, 255, 255))


    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 3)

    
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, (0, 0, 0))
                screen.blit(text, (col * 100 + 30, row * 100 + 20))


    if winner:
        text = small_font.render(f"{winner} WINS!",True,(0,150,0))
        screen.blit(text,(80,130))
    pygame.display.update()

pygame.quit()
