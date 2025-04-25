import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 550
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Fill Puzzle")

font = pygame.font.Font(None, 48)

board = [[None for _ in range(COLS)] for _ in range(ROWS)]

def is_valid_color(row, col, color):
    neighbors = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    for r, c in neighbors:
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == color:
            return False
    return True

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = board[row][col] if board[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)

def draw_color_selector(selected_color):
    selector_height = 50
    for i, color in enumerate(COLORS):
        x = i * (WIDTH // len(COLORS))
        rect = pygame.Rect(x, HEIGHT - selector_height, WIDTH // len(COLORS), selector_height)
        pygame.draw.rect(screen, color, rect)
        if color == selected_color:
            pygame.draw.rect(screen, BLACK, rect, 5)

def show_end_message(win):
    screen.fill(WHITE)
    message = "You Win!" if win else "You Lose!"
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

def main():
    running = True
    selected_color = COLORS[0]
    game_over = False

    while running:
        screen.fill(WHITE)
        draw_board()
        draw_color_selector(selected_color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if y > HEIGHT - 50:
                        index = x // (WIDTH // len(COLORS))
                        if 0 <= index < len(COLORS):
                            selected_color = COLORS[index]
                    else:
                        row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                        if selected_color and is_valid_color(row, col, selected_color):
                            board[row][col] = selected_color

                            if all(all(cell is not None for cell in row) for row in board):
                                game_over = True
                                show_end_message(True)
                        else:
                            game_over = True
                            show_end_message(False)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
