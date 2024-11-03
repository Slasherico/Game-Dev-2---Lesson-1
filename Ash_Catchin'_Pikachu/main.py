import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIKACHU_WIDTH = 50
PIKACHU_HEIGHT = 50
BUSH_WIDTH = 70
BUSH_HEIGHT = 40
CLOUD_WIDTH = 100
CLOUD_HEIGHT = 50
ASH_WIDTH = 50  # Adjust width for Ash
ASH_HEIGHT = 80  # Adjust height for Ash
POKEBALL_WIDTH = 30  # Adjust width for Pokéball
POKEBALL_HEIGHT = 30  # Adjust height for Pokéball
GAME_DURATION = 30  # seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
pikachu_image = pygame.image.load('pikachu.png')  # Ensure you have a Pikachu image
pikachu_image = pygame.transform.scale(pikachu_image, (PIKACHU_WIDTH, PIKACHU_HEIGHT))
bush_image = pygame.image.load('bush.png')  # Ensure you have a Bush image
bush_image = pygame.transform.scale(bush_image, (BUSH_WIDTH, BUSH_HEIGHT))
cloud_image = pygame.image.load('cloud.png')  # Ensure you have a Cloud image
cloud_image = pygame.transform.scale(cloud_image, (CLOUD_WIDTH, CLOUD_HEIGHT))
ash_image = pygame.image.load('ash.png')  # Ensure you have an Ash image
ash_image = pygame.transform.scale(ash_image, (ASH_WIDTH, ASH_HEIGHT))
pokeball_image = pygame.image.load('pokeball.png')  # Ensure you have a Pokéball image
pokeball_image = pygame.transform.scale(pokeball_image, (POKEBALL_WIDTH, POKEBALL_HEIGHT))

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch Pikachu!")

# Game variables
score = 0
game_active = True
start_time = time.time()

# Function to draw clouds at fixed positions
cloud_positions = []
cloud_directions = []  # To store the direction of each cloud

def draw_sky():
    screen.fill(WHITE)  # Fill the background with white (sky)
    for cloud in cloud_positions:
        screen.blit(cloud_image, cloud)

def initialize_clouds():
    for _ in range(5):  # Initialize 5 clouds at random positions
        cloud_x = random.randint(0, SCREEN_WIDTH - CLOUD_WIDTH)
        cloud_y = random.randint(0, SCREEN_HEIGHT // 4)
        cloud_positions.append((cloud_x, cloud_y))
        cloud_directions.append(1)  # Initially move to the right

def update_clouds():
    for i in range(len(cloud_positions)):
        # Move clouds left or right
        cloud_x, cloud_y = cloud_positions[i]
        if cloud_x >= SCREEN_WIDTH - CLOUD_WIDTH:  # Hit the right edge
            cloud_directions[i] = -1  # Change direction to left
        elif cloud_x <= 0:  # Hit the left edge
            cloud_directions[i] = 1  # Change direction to right
        cloud_positions[i] = (cloud_x + cloud_directions[i], cloud_y)

# Function to draw Pikachu at a random position
def draw_pikachu():
    pikachu_x = random.randint(0, SCREEN_WIDTH - PIKACHU_WIDTH)
    pikachu_y = random.randint(0, SCREEN_HEIGHT - PIKACHU_HEIGHT)
    return (pikachu_x, pikachu_y)

# Function to generate multiple bushes
def generate_bushes(num_bushes):
    bushes = []
    for _ in range(num_bushes):
        bush_x = random.randint(0, SCREEN_WIDTH - BUSH_WIDTH)
        bush_y = random.randint(0, SCREEN_HEIGHT - BUSH_HEIGHT)
        bushes.append((bush_x, bush_y))
    return bushes

# Function to move bushes randomly
def move_bushes(bushes, cloud_positions):
    # Find the lowest cloud position
    lowest_cloud_y = max(cloud_y for _, cloud_y in cloud_positions) + CLOUD_HEIGHT
    new_bushes = []
    for _ in range(len(bushes)):
        bush_x = random.randint(0, SCREEN_WIDTH - BUSH_WIDTH)
        bush_y = random.randint (lowest_cloud_y, SCREEN_HEIGHT - BUSH_HEIGHT)
        new_bushes.append((bush_x, bush_y))
    return new_bushes

# Main game loop
def game_loop():
    global score, game_active, start_time
    clock = pygame.time.Clock()
    pikachu_position = draw_pikachu()  # Initialize Pikachu's position
    bushes = generate_bushes(10)  # Generate 10 bushes
    initialize_clouds()  # Initialize clouds

    while game_active:
        draw_sky()  # Draw the sky and clouds
        update_clouds()  # Update cloud positions

        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = GAME_DURATION - elapsed_time

        # Check for game duration
        if remaining_time <= 0:
            game_active = False
            break

        # Draw bushes
        for bush_position in bushes:
            screen.blit(bush_image, bush_position)  # Draw each bush

        # Draw Pikachu
        screen.blit(pikachu_image, pikachu_position)  # Draw Pikachu

        # Draw Ash at the bottom left
        screen.blit(ash_image, (10, SCREEN_HEIGHT - ASH_HEIGHT - 10))  # Draw Ash
        screen.blit(pokeball_image, (ASH_WIDTH + 20, SCREEN_HEIGHT - POKEBALL_HEIGHT - 10))  # Draw Pokéball

        # Display score and remaining time
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        time_text = font.render(f"Time: {int(remaining_time)} seconds", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 40))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (pikachu_position[0] <= mouse_x <= pikachu_position[0] + PIKACHU_WIDTH and
                    pikachu_position[1] <= mouse_y <= pikachu_position[1] + PIKACHU_HEIGHT):
                    score += 1
                    pikachu_position = draw_pikachu()  # Move Pikachu to a new position
                    bushes = move_bushes(bushes, cloud_positions)  # Move bushes randomly

        pygame.display.flip()
        clock.tick(30)  # Limit to 30 frames per second

    # Game over
    print(f"Game Over! Your score: {score}")
    pygame.quit()

# Start the game
game_loop()