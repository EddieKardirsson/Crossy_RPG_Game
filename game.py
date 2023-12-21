import pygame
from gameObject import GameObject


class Game:

    def __init__(self, resolution):

        # refactored the resolution variables back to main.py
        self.resolution = resolution

        # change resolution/screen size with this variable
        self.current_display_size = self.resolution
        self.center_position = (self.current_display_size[0] / 2, self.current_display_size[1] / 2)

        self.white_colour = (255, 255, 255)
        self.black_colour = (0, 0, 0)  # using black colour background initially because it is easier to the eye

        self.game_window = pygame.display.set_mode(self.current_display_size)

        self.clock = pygame.time.Clock()

        self.BACKGROUND_CENTER_POS = 0.22
        self.OBJECT_SCALE_FACTOR = self.current_display_size[1] * 0.004
        self.TREASURE_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.08)

        # load the background image to a variable
        self.background = GameObject(
            self.current_display_size[0] * self.BACKGROUND_CENTER_POS,
            0,
            self.current_display_size[1],
            self.current_display_size[1],
            "Assets/background.png"
        )

        self.treasure = GameObject(
            self.TREASURE_POS[0],
            self.TREASURE_POS[1],
            0,
            0,
            "Assets/treasure.png",
            self.OBJECT_SCALE_FACTOR
        )

        # treasure_image = pygame.image.load("Assets/treasure.png")
        # self.treasure = pygame.transform.scale(treasure_image, (
        #     treasure_image.get_width() * self.OBJECT_SCALE_FACTOR,
        #     treasure_image.get_height() * self.OBJECT_SCALE_FACTOR))

    def update_display(self):
        self.game_window.fill(self.black_colour)
        # self.game_window.blit(self.background, (self.current_display_size[0] * self.BACKGROUND_CENTER_POS, 0))
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        # self.game_window.blit(self.treasure, self.TREASURE_POS)
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
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
