import pygame


class Game:

    def __init__(self):
        self.resolution_4k = (3840, 2160)
        self.resolution_2k = (2560, 1440)
        self.resolution_1080p = (1920, 1080)
        self.resolution_720p = (1280, 720)

        # change resolution/screen size with this variable
        self.current_display_size = self.resolution_2k
        self.center_position = (self.current_display_size[0] / 2, self.current_display_size[1] / 2)

        self.white_colour = (255, 255, 255)
        self.black_colour = (0, 0, 0)  # using black colour background initially because it is easier to the eye

        self.game_window = pygame.display.set_mode(self.current_display_size)

        self.clock = pygame.time.Clock()

        # load the background image to a variable
        background_image = pygame.image.load("Assets/background.png")
        # Scale the background image with the height value (lowest scaling value)
        self.background = pygame.transform.scale(background_image, (
            self.current_display_size[1],
            self.current_display_size[1]))
        # center factor to position the image to the middle.
        self.BACKGROUND_CENTER_POS = 0.22  # After a little trial and error, this constant works perfect to center the X-position
        self.OBJECT_SCALE_FACTOR = self.current_display_size[1] * 0.004

        treasure_image = pygame.image.load("Assets/treasure.png")
        self.treasure = pygame.transform.scale(treasure_image, (
            treasure_image.get_width() * self.OBJECT_SCALE_FACTOR,
            treasure_image.get_height() * self.OBJECT_SCALE_FACTOR))
        self.TREASURE_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.08)

    def update_display(self):
        self.game_window.fill(self.black_colour)
        self.game_window.blit(self.background, (self.current_display_size[0] * self.BACKGROUND_CENTER_POS, 0))
        self.game_window.blit(self.treasure, self.TREASURE_POS)
        pygame.display.update()

    def run_game_loop(self):
        while True:

            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return

            # Execute logic

            # Update display
            self.update_display()

            self.clock.tick(60)
