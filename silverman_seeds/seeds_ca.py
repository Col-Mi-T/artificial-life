def seeds():
    from silverman_seeds.seeds import grid
    import pygame
    pygame.init()


    clock = pygame.time.Clock()


    running = True
    life = grid.life
    gen = [row[:] for row in life]

    HEIGHT = len(life)
    WIDTH = len(life[0])

    CELL_SIZE = 20

    screen = pygame.display.set_mode((
        WIDTH * CELL_SIZE,
        HEIGHT * CELL_SIZE + 50
    ))
    font = pygame.font.SysFont("Arial", 24)

    generation = 0
    highest = 0
    while running:
        generation += 1
        population = 0
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
        In each time step, a cell turns on or is "born" if it was off or "dead" but had exactly two neighbours
        that were on; all other cell turn off (B2/S).
        """
        left, middle, right = pygame.mouse.get_pressed()

        if left:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            grid_x = mouse_x // CELL_SIZE
            grid_y = mouse_y // CELL_SIZE
            if 0 <= grid_x < WIDTH and 0 <= grid_y < HEIGHT:
                if life[grid_y][grid_x] == 0:
                    life[grid_y][grid_x] = 1
                elif life[grid_y][grid_x] == 1:
                    life[grid_y][grid_x] = 0
        
        for y, row in enumerate(life):
            for x, cell in enumerate(row):
                if cell == 1:
                    population += 1
                neighbours = 0

                # Top-left
                neighbours += life[(y-1) % HEIGHT][(x-1) % WIDTH]

                # Top
                neighbours += life[(y-1) % HEIGHT][x]

                # Top-right
                neighbours += life[(y-1) % HEIGHT][(x+1) % WIDTH]

                # Left
                neighbours += life[y][(x-1) % WIDTH]

                # Right
                neighbours += life[y][(x+1) % WIDTH]

                # Bottom-left
                neighbours += life[(y+1) % HEIGHT][(x-1) % WIDTH]

                # Bottom
                neighbours += life[(y+1) % HEIGHT][x]

                # Bottom-right
                neighbours += life[(y+1) % HEIGHT][(x+1) % WIDTH]

                if neighbours == 2 and cell == 0
                #if neighbours >= 2 and neighbours<=4 and cell == 0: # My personal variation of this... seems more explosive
                    gen[y][x] = 1
                
                elif cell == 1:
                    gen[y][x] = 0
                    
            

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

        if population > highest:
            highest = population
        text = font.render(f"Generation:{generation} Population:{population} Highest:{highest}", True, (255, 0, 0))
        screen.blit(text, (10,HEIGHT*CELL_SIZE+10))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

