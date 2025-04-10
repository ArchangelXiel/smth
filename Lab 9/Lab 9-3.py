import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Program")

clock = pygame.time.Clock()
drawing = False
last_pos = None
color = (0, 0, 0)
brush_size = 5
mode = 'brush'  # modes: brush, rectangle, circle, eraser, square, right_triangle, equilateral_triangle, rhombus

canvas = pygame.Surface(screen.get_size())
canvas.fill((255, 255, 255))

start_shape = None

# Color palette
colors = {
    pygame.K_1: (0, 0, 0),
    pygame.K_2: (255, 0, 0),
    pygame.K_3: (0, 255, 0),
    pygame.K_4: (0, 0, 255),
    pygame.K_5: (255, 255, 0),
}

def draw_square(start_pos, end_pos):
    size = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    pygame.draw.rect(canvas, color, pygame.Rect(start_pos[0], start_pos[1], size, size), 2)

def draw_right_triangle(start_pos, end_pos):
    size = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    points = [(start_pos[0], start_pos[1]), 
              (start_pos[0] + size, start_pos[1]), 
              (start_pos[0], start_pos[1] - size)]
    pygame.draw.polygon(canvas, color, points, 2)

def draw_equilateral_triangle(start_pos, end_pos):
    size = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    height = (size * (3 ** 0.5)) / 2
    points = [(start_pos[0], start_pos[1]), 
              (start_pos[0] + size, start_pos[1]), 
              (start_pos[0] + size / 2, start_pos[1] - height)]
    pygame.draw.polygon(canvas, color, points, 2)

def draw_rhombus(start_pos, end_pos):
    size = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    points = [(start_pos[0], start_pos[1] - size // 2), 
              (start_pos[0] + size // 2, start_pos[1]), 
              (start_pos[0], start_pos[1] + size // 2), 
              (start_pos[0] - size // 2, start_pos[1])]
    pygame.draw.polygon(canvas, color, points, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            start_shape = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_shape = event.pos
            if mode == 'rectangle':
                rect = pygame.Rect(min(start_shape[0], end_shape[0]),
                                   min(start_shape[1], end_shape[1]),
                                   abs(start_shape[0] - end_shape[0]),
                                   abs(start_shape[1] - end_shape[1]))
                pygame.draw.rect(canvas, color, rect, 2)
            elif mode == 'circle':
                radius = int(((start_shape[0] - end_shape[0]) ** 2 + (start_shape[1] - end_shape[1]) ** 2) ** 0.5)
                pygame.draw.circle(canvas, color, start_shape, radius, 2)
            elif mode == 'square':
                draw_square(start_shape, end_shape)
            elif mode == 'right_triangle':
                draw_right_triangle(start_shape, end_shape)
            elif mode == 'equilateral_triangle':
                draw_equilateral_triangle(start_shape, end_shape)
            elif mode == 'rhombus':
                draw_rhombus(start_shape, end_shape)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'brush':
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif mode == 'eraser':
                pygame.draw.line(canvas, (255, 255, 255), last_pos, event.pos, brush_size)
                last_pos = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_b:
                mode = 'brush'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_triangle'
            elif event.key == pygame.K_q:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                mode = 'rhombus'
            elif event.key in colors:
                color = colors[event.key]

    screen.blit(canvas, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
