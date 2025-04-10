import pygame
import random

pygame.init()

# Screen settings
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer with Coins")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

# Load player car
player = pygame.Rect(160, 480, 40, 80)
player_speed = 5

# Enemy car
enemy = pygame.Rect(random.randint(40, 320), 0, 40, 80)
enemy_speed = 5

# Coins
coins = []
coin_size = 20
coin_timer = 0
coin_interval = 50
collected_coins = 0

# Game state
running = True
game_over = False

while running:
    screen.fill(gray)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 40:
            player.move_ip(-player_speed, 0)
        if keys[pygame.K_RIGHT] and player.right < 360:
            player.move_ip(player_speed, 0)

        # Move enemy
        enemy.move_ip(0, enemy_speed)
        if enemy.top > height:
            enemy.top = 0
            enemy.left = random.randint(40, 320)

        # Check collision with enemy
        if player.colliderect(enemy):
            game_over = True

        # Add coins
        coin_timer += 1
        if coin_timer >= coin_interval:
            coin_x = random.randint(40, 360 - coin_size)
            coins.append(pygame.Rect(coin_x, 0, coin_size, coin_size))
            coin_timer = 0

        # Move coins and check collision
        for coin in coins[:]:
            coin.move_ip(0, 5)
            if player.colliderect(coin):
                coins.remove(coin)
                collected_coins += 1
            elif coin.top > height:
                coins.remove(coin)

        # Draw road lines
        for y in range(0, height, 60):
            pygame.draw.line(screen, white, (200, y), (200, y + 30), 3)

        # Draw player and enemy
        pygame.draw.rect(screen, red, player)
        pygame.draw.rect(screen, black, enemy)

        # Draw coins
        for coin in coins:
            pygame.draw.circle(screen, yellow, coin.center, coin_size // 2)

        # Draw score
        coin_text = font.render(f"Coins: {collected_coins}", True, white)
        screen.blit(coin_text, (width - 130, 10))
    else:
        # Display game over text
        over_text = font.render("Game Over!", True, red)
        screen.blit(over_text, (width // 2 - 70, height // 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
