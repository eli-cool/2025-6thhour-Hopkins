#Name: ELi Hopkins
#Class: 6th Hour
#Assignment: AI playground
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
car_width = 50
car_height = 100
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 5
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 5
score = 0

# Clock
clock = pygame.time.Clock()

# Load car image
car_img = pygame.Surface((car_width, car_height))
car_img.fill(RED)

# Function to draw the car
def draw_car(x, y):
    screen.blit(car_img, (x, y))

# Function to generate a new obstacle
def generate_obstacle():
    x = random.randint(0, screen_width - obstacle_width)
    return [x, -obstacle_height]

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height))

# Function to update obstacle positions
def update_obstacles(obstacles):
    global score
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            obstacles.append(generate_obstacle())
            score += 1

# Function to display the score
def display_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
def game_loop():
    global car_x, car_y, score
    obstacles = [generate_obstacle() for _ in range(10)]  # Start with 3 obstacles
    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key states
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed

        # Update obstacles
        update_obstacles(obstacles)

        # Check for collisions
        for obstacle in obstacles:
            if car_x < obstacle[0] + obstacle_width and car_x + car_width > obstacle[0] and car_y < obstacle[1] + obstacle_height and car_y + car_height > obstacle[1]:
                running = False  # Game over

        # Draw everything
        draw_car(car_x, car_y)
        draw_obstacles(obstacles)
        display_score()

        # Update the screen
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
game_loop()