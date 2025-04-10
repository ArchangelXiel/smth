import pygame
import random

pygame.init()

# Screen settings
cell_size = 20
cols, rows = 30, 20
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
pygame.display.set_caption("Snake Game with Levels")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Initial snake and food setup
snake = [(5, 5)]
direction = (1, 0)
food = (random.randint(0, cols - 1), random.randint(0, rows - 1))

# Score and level
score = 0
level = 1
speed = 10

# Font
font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()
running = True

# Generate a new food not on snake
def generate_food():
    while True:
        new_food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if new_food not in snake:
            return new_food

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move the snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for wall collision
    if not (0 <= new_head[0] < cols and 0 <= new_head[1] < rows):
        running = False
        continue

    # Check for self collision
    if new_head in snake:
        running = False
        continue

    snake.insert(0, new_head)

    # Eating food
    if new_head == food:
        score += 1
        food = generate_food()

        # Increase level and speed
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Drawing
    screen.fill(black)

    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, green, (block[0] * cell_size, block[1] * cell_size, cell_size, cell_size))

    # Draw food
    pygame.draw.rect(screen, red, (food[0] * cell_size, food[1] * cell_size, cell_size, cell_size))

    # Draw score and level
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()