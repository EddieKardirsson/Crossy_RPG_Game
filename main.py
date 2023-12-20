import pygame

pygame.init()

resolution_4k = (3840, 2160)
resolution_2k = (2560, 1440)
resolution_1080p = (1920, 1080)
resolution_720p = (1280, 720)

# change resolution/screen size with this variable
current_display_size = resolution_2k
center_position = (current_display_size[0]/2, current_display_size[1]/2)

white_colour = (255, 255, 255)
black_colour = (0, 0, 0)  # using black colour background initially because it is easier to the eye

game_window = pygame.display.set_mode(current_display_size)

clock = pygame.time.Clock()

# load the background image to a variable
background_image = pygame.image.load("Assets/background.png")
# Scale the background image with the height value (lowest scaling value)
background = pygame.transform.scale(background_image, (current_display_size[1], current_display_size[1]))
# center factor to position the image to the middle.
BACKGROUND_CENTER_POS = 0.22     # After a little trial and error, this constant works perfect to center the X-position

OBJECT_SCALE_FACTOR = current_display_size[1] * 0.004

treasure_image = pygame.image.load("Assets/treasure.png")
treasure = pygame.transform.scale(treasure_image, (
    treasure_image.get_width() * OBJECT_SCALE_FACTOR,
    treasure_image.get_height() * OBJECT_SCALE_FACTOR))
TREASURE_POS = (current_display_size[0]*0.485, current_display_size[1]*0.08)


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
        game_window.blit(background, (current_display_size[0]*BACKGROUND_CENTER_POS, 0))
        game_window.blit(treasure, TREASURE_POS)
        pygame.display.update()

        clock.tick(60)


run_game_loop()

pygame.quit()
quit()
