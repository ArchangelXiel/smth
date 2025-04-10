import pygame
import random
import time

pygame.init()

# Screen setup
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Weighted Food")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 155, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Snake settings
snake_block = 20
snake_speed = 10
snake = [(300, 200), (280, 200), (260, 200)]
snake_dir = (0, 0)

# Food (rect, weight, spawn_time)
foods = []
food_lifetime = 5
score = 0

# Game loop
running = True
game_over = False

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Snake controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dir != (snake_block, 0):
                snake_dir = (-snake_block, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-snake_block, 0):
                snake_dir = (snake_block, 0)
            elif event.key == pygame.K_UP and snake_dir != (0, snake_block):
                snake_dir = (0, -snake_block)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -snake_block):
                snake_dir = (0, snake_block)

    if not game_over:
        # Move snake
        if snake_dir != (0, 0):
            new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
            snake = [new_head] + snake[:-1]

        # Collision with walls
        if (snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height):
            game_over = True

        # Collision with itself
        if snake[0] in snake[1:]:
            game_over = True

        # Randomly spawn food
        if len(foods) < 3 and random.randint(0, 30) == 0:
            x = random.randint(0, (width - snake_block) // snake_block) * snake_block
            y = random.randint(0, (height - snake_block) // snake_block) * snake_block
            weight = random.choice([1, 2, 3])
            spawn_time = time.time()
            if (x, y) not in snake:
                foods.append([(x, y), weight, spawn_time])

        # Remove expired food
        current_time = time.time()
        foods = [f for f in foods if current_time - f[2] <= food_lifetime]

        # Check if food eaten
        for f in foods[:]:
            if snake[0] == f[0]:
                score += f[1]
                foods.remove(f)
                for _ in range(f[1]):
                    snake.append(snake[-1])

        # Draw snake (head is dark green)
        pygame.draw.rect(screen, dark_green, (snake[0][0], snake[0][1], snake_block, snake_block))
        for segment in snake[1:]:
            pygame.draw.rect(screen, green, (segment[0], segment[1], snake_block, snake_block))

        # Draw food with different colors based on weight
        for f in foods:
            food_color = red if f[1] == 1 else orange if f[1] == 2 else blue
            pygame.draw.rect(screen, food_color, (f[0][0], f[0][1], snake_block, snake_block))

        # Draw score
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))
    else:
        # Game over message
        over_text = font.render("Game Over!", True, red)
        screen.blit(over_text, (width // 2 - 60, height // 2))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
