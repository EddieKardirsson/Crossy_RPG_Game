import pygame

pygame.init()

resolution_4k = (3840, 2160)
resolution_2k = (2560, 1440)
resolution_1080p = (1920, 1080)
resolution_720p = (1280, 720)

# change resolution/screen size with this variable
current_display_size = resolution_2k

white_colour = (255, 255, 255)
black_colour = (0, 0, 0)  # using black colour background initially because it is easier to the eye

game_window = pygame.display.set_mode(current_display_size)

clock = pygame.time.Clock()


def run_game_loop():
    while True:

        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # Execute logic

        # Update display
        game_window.fill(black_colour)
        pygame.display.update()

        clock.tick(60)


run_game_loop()

pygame.quit()
quit()
