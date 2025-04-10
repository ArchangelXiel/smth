import pygame

pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Ball Movement")

ball_radius = 25
ball_color = (255, 0, 0)
background_color = (255, 255, 255)
ball_pos = [screen_width // 2, screen_height // 2]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_pos[1] - ball_radius - 20 >= 0:
        ball_pos[1] -= 20
    if keys[pygame.K_DOWN] and ball_pos[1] + ball_radius + 20 <= screen_height:
        ball_pos[1] += 20
    if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius - 20 >= 0:
        ball_pos[0] -= 20
    if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius + 20 <= screen_width:
        ball_pos[0] += 20

    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
