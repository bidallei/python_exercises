import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Colores
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128)
]

# Formas de las piezas
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Función para crear una nueva pieza
def new_piece():
    shape = random.choice(shapes)
    color = random.choice(colors[1:])
    return {'shape': shape, 'color': color, 'x': 3, 'y': 0}

# Rotar la pieza
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Comprobar colisión
def collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if y + off_y >= len(board) or x + off_x >= len(board[0]) or x + off_x < 0:
                    return True
                if y + off_y >= 0 and board[y + off_y][x + off_x]:
                    return True
    return False

# Eliminar filas completas
def remove_full_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    removed_rows = len(board) - len(new_board)
    new_board = [[0 for _ in range(10)] for _ in range(removed_rows)] + new_board
    return new_board, removed_rows

# Función principal del juego
def run_game():
    clock = pygame.time.Clock()
    board = [[0 for _ in range(10)] for _ in range(20)]
    current_piece = new_piece()
    next_piece = new_piece()
    score = 0
    game_over = False

    while not game_over:
        screen.fill((0, 0, 0))

        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece['x'] -= 1
                    if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
                        current_piece['x'] += 1
                if event.key == pygame.K_RIGHT:
                    current_piece['x'] += 1
                    if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
                        current_piece['x'] -= 1
                if event.key == pygame.K_DOWN:
                    current_piece['y'] += 1
                    if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
                        current_piece['y'] -= 1
                if event.key == pygame.K_UP:
                    current_piece['shape'] = rotate(current_piece['shape'])
                    if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
                        current_piece['shape'] = rotate(current_piece['shape'])[::-1]

        # Movimiento automático hacia abajo
        current_piece['y'] += 1
        if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
            current_piece['y'] -= 1
            for y, row in enumerate(current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        board[y + current_piece['y']][x + current_piece['x']] = current_piece['color']
            board, removed_rows = remove_full_rows(board)
            score += removed_rows * 10
            current_piece = next_piece
            next_piece = new_piece()
            if collision(board, current_piece['shape'], (current_piece['x'], current_piece['y'])):
                game_over = True

        # Dibujar el tablero
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, pygame.Rect(x * block_size, y * block_size, block_size, block_size))

        # Dibujar la pieza actual
        for y, row in enumerate(current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_piece['color'], pygame.Rect((current_piece['x'] + x) * block_size, (current_piece['y'] + y) * block_size, block_size, block_size))

        pygame.display.flip()
        clock.tick(1)

    print("Game Over. Score:", score)

run_game()
pygame.quit()