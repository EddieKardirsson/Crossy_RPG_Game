import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


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

        enemy_image_path = "Assets/enemy.png"
        self.BACKGROUND_CENTER_POS = 0.22
        self.OBJECT_SCALE_FACTOR = self.current_display_size[1] * 0.004
        self.TREASURE_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.08)
        self.PLAYER_START_POS = (self.current_display_size[0] * 0.488, self.current_display_size[1] * (1 - 0.08))

        self.ENEMY_X_BOUNDS = (self.current_display_size[0] * 0.28, self.current_display_size[0] * 0.72)

        self.ENEMY1_START_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.70)

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

        self.player = Player(
            self.PLAYER_START_POS[0],
            self.PLAYER_START_POS[1],
            0,
            0,
            "Assets/player.png",
            5,
            self.OBJECT_SCALE_FACTOR
        )

        self.enemies = [
            Enemy(
                self.ENEMY1_START_POS[0],
                self.ENEMY1_START_POS[1],
                0,
                0,
                enemy_image_path,
                5,
                self.OBJECT_SCALE_FACTOR
            )
        ]

    def update_display(self):
        self.game_window.fill(self.black_colour)
        # self.game_window.blit(self.background, (self.current_display_size[0] * self.BACKGROUND_CENTER_POS, 0))
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        # self.game_window.blit(self.treasure, self.TREASURE_POS)
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.enemies[0].image, (self.enemies[0].x, self.enemies[0].y))
        pygame.display.update()

    def run_game_loop(self):
        player_direction = 0

        while True:

            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player_direction = 0
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player_direction = 0

            # Execute logic
            self.player.move(player_direction, self.current_display_size[1])
            self.enemies[0].move(self.ENEMY_X_BOUNDS)

            # Update display
            self.update_display()

            self.clock.tick(60)
