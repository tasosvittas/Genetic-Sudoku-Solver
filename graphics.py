import pygame
import sys

# Initialize the pygame font
pygame.font.init()

# Total window dimensions
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
GRID_SIZE = 9

# Set up the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SUDOKU DISPLAY")

# Constants for difficulties
DIFFICULTIES = {
    "Beginner": [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
    "Medium": [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
        [0, 5, 0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 3, 7, 0, 0, 0, 0, 4, 0],
        [0, 0, 4, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    "Expert": [
        [0, 2, 0, 0, 0, 8, 0, 0, 3],
        [0, 0, 0, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 1, 0, 0, 5, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 5],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 2, 0]
    ]
}

# Initialize variables
x, y = -1, -1  # Prevent initial cell from being selected
dif = WINDOW_WIDTH / GRID_SIZE
grid = []  # Current Sudoku grid to work with
original_grid = []  # Original Sudoku grid to reset to

# Load fonts for numbers and instructions
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
    global x, y
    x = int(pos[0] // dif)  # Ensure x is an integer (column)
    y = int(pos[1] // dif)  # Ensure y is an integer (row)

# Highlight the cell selected
def draw_box():
    if x != -1 and y != -1:  # Only draw the box if a cell is selected
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

# Function to draw the Sudoku grid and fill in numbers
def draw():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Draw filled cells
            if grid[j][i] != 0:  # Notice the indexing is (j, i) for grid[row][column]
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))  # Background for filled cells
                text1 = font1.render(str(grid[j][i]), 1, (0, 0, 0))  # Render number
                screen.blit(text1, (i * dif + 15, j * dif + 15))  # Draw the number

    # Draw grid lines
    for i in range(GRID_SIZE + 1):
        thick = 7 if i % 3 == 0 else 1  # Thicker lines for 3x3 boxes
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (WINDOW_WIDTH, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, WINDOW_HEIGHT - 100), thick)

# Function to display instructions
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("CLICK ON A CELL AND ENTER A NUMBER (1-9)", 1, (0, 0, 0))
    screen.blit(text1, (20, WINDOW_HEIGHT - 80))
    screen.blit(text2, (20, WINDOW_HEIGHT - 60))

# Draw the difficulty selection screen
def draw_menu():
    screen.fill((255, 255, 255))  # White background
    title_font = pygame.font.SysFont("comicsans", 50)
    title_text = title_font.render("Select Difficulty", True, (0, 0, 0))
    screen.blit(title_text, (50, 50))

    for i, (difficulty, _) in enumerate(DIFFICULTIES.items()):
        button_text = font2.render(difficulty, True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 153, 153), (50, 150 + i * 60, 400, 50))  # Button background
        screen.blit(button_text, (75, 160 + i * 60))  # Button text

# Main game loop
def main():
    global grid, original_grid

    # Draw the menu
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, (difficulty, _) in enumerate(DIFFICULTIES.items()):
                    if 50 <= pos[0] <= 450 and (150 + i * 60) <= pos[1] <= (200 + i * 60):
                        grid = DIFFICULTIES[difficulty]  # Set the grid based on difficulty
                        original_grid = [row[:] for row in grid]  # Store a copy of the original grid for resetting
                        game_loop()  # Enter the Sudoku game loop

        pygame.display.update()

# Game loop for Sudoku
def game_loop():
    global x, y, grid  # Declare grid as global
    while True:
        screen.fill((255, 255, 255))  # White background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Get mouse position and determine selected cell
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                get_cord(pos)  # Set x and y based on mouse position

            # Get the number to be inserted if key pressed
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                    # Ensure we're accessing the grid correctly
                    if x != -1 and y != -1 and grid[y][x] == 0:  # Check if the cell is empty
                        grid[y][x] = event.key - pygame.K_0  # Correctly set the selected cell
                        print(f"Updated grid at ({y}, {x}) with {grid[y][x]}")  # Debugging line
                        print(grid)  # Print the entire grid for verification

                # Reset the grid to original when 'D' is pressed
                if event.key == pygame.K_d:
                    grid = original_grid  # Reset to the original grid

                # Reset to empty when 'R' is pressed
                if event.key == pygame.K_r:
                    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Empty grid

        # Draw the grid and numbers
        draw()

        # Highlight the selected cell
        draw_box()

        # Display instructions
        instruction()

        pygame.display.update()

# Start the game
main()
