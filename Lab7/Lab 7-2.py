import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Music Player")

music_files = [f for f in os.listdir(".") if f.endswith(".mp3") or f.endswith(".ogg")]
current_index = 0

pygame.mixer.init()

running = True
playing = False

if music_files:
    pygame.mixer.music.load(music_files[current_index])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not playing:
                    pygame.mixer.music.play()
                    playing = True
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

            elif event.key == pygame.K_n:
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_index])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_b:
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_index])
                pygame.mixer.music.play()
                playing = True

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
