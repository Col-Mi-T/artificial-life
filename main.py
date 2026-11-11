import grid
import pygame
import sys
sys.dont_write_bytecode = True
pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

running = True
life = grid.life
gen = [row[:] for row in life]

HEIGHT = len(life)
WIDTH = len(life[0])

CELL_SIZE = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20,20,20))

    # Create a fresh generation
    gen = [[0 for cell in row] for row in life]

    """
    A cell has 8 neighbours:

    life[row-1][cell-1]   Top-left
    life[row-1][cell]     Top
    life[row-1][cell+1]   Top-right

    life[row][cell-1]     Left
    life[row][cell+1]     Right

    life[row+1][cell-1]   Bottom-left
    life[row+1][cell]     Bottom
    life[row+1][cell+1]   Bottom-right

    Rules:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    for y, row in enumerate(life):
        for x, cell in enumerate(row):
            neighbours = 0

            # Top-left
            if y > 0 and x > 0:
                neighbours += life[y-1][x-1]

            # Top
            if y > 0:
                neighbours += life[y-1][x]

            # Top-right
            if y > 0 and x < WIDTH-1:
                neighbours += life[y-1][x+1]

            # Left
            if x > 0:
                neighbours += life[y][x-1]

            # Right
            if x < WIDTH-1:
                neighbours += life[y][x+1]

            # Bottom-left
            if y < HEIGHT-1 and x > 0:
                neighbours += life[y+1][x-1]

            # Bottom
            if y < HEIGHT-1:
                neighbours += life[y+1][x]

            # Bottom-right
            if y < HEIGHT-1 and x < WIDTH-1:
                neighbours += life[y+1][x+1]

            # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if neighbours < 2 and cell == 1:
                gen[y][x] = 0

            # 2. Any live cell with two or three live neighbours lives on to the next generation.
            elif neighbours in [2,3] and cell == 1:
                gen[y][x] = 1

            # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
            elif neighbours > 3 and cell == 1:
                gen[y][x] = 0

            # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            elif neighbours == 3 and cell == 0:
                gen[y][x] = 1

    # Synchronise generations
    life = gen

    for y, row in enumerate(life):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(
                    screen,
                    (0,255,0),
                    (
                        x*CELL_SIZE,
                        y*CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )

            else:
                pygame.draw.rect(
                    screen,
                    (255,255,255),
                    (
                        x*CELL_SIZE,
                        y*CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )

            pygame.draw.rect(
                screen,
                (50,50,50),
                (
                    x*CELL_SIZE,
                    y*CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                ),
                1
            )

    pygame.display.flip()
    clock.tick(3)

pygame.quit()
