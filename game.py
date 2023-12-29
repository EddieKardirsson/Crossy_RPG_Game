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

        self.enemy_image_path = "Assets/enemy.png"
        self.BACKGROUND_CENTER_POS = 0.22
        self.OBJECT_SCALE_FACTOR = self.current_display_size[1] * 0.004
        self.TREASURE_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.08)
        self.PLAYER_START_POS = (self.current_display_size[0] * 0.488, self.current_display_size[1] * (1 - 0.08))

        self.X_BOUNDS = (self.current_display_size[0] * 0.28, self.current_display_size[0] * 0.72)

        self.ENEMY0_START_POS = (self.current_display_size[0] * 0.485, self.current_display_size[1] * 0.70)
        self.ENEMY1_START_POS = (self.current_display_size[0] * 0.285, self.current_display_size[1] * 0.50)
        self.ENEMY2_START_POS = (self.current_display_size[0] * 0.685, self.current_display_size[1] * 0.30)

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

        self.base_speed = 5
        self.resolution_speed = self.get_resolution_speed()
        self.level = 1.0
        self.reset_map()

    # even with a fixed framerate, bug appeared due to resolution size where smaller went faster while
    # larger went slower. This function does adjust it. Not the best solution but for such a microscopic
    # game like this one, it doesn't matter that much. At least it works! :)
    def get_resolution_speed(self):
        if self.resolution[1] == 720:
            return 0
        elif self.resolution[1] == 1080:
            return 4
        elif self.resolution[1] == 1440:
            return 8
        elif self.resolution[1] == 2160:
            return 12
        return 0

    def reset_map(self):

        self.player = self.get_player()
        speed = self.resolution_speed + (self.level * self.base_speed)

        if self.level >= 4.0:
            self.enemies = self.get_enemies(speed, 3)
        elif self.level >= 2.0:
            self.enemies = self.get_enemies(speed, 2)
        else:
            self.enemies = self.get_enemies(speed, 1)

    def get_player(self):
        return Player(
            self.PLAYER_START_POS[0],
            self.PLAYER_START_POS[1],
            0,
            0,
            "Assets/player.png",
            self.base_speed + self.resolution_speed,
            self.OBJECT_SCALE_FACTOR
        )

    def get_enemies(self, speed, index):
        max_enemies = [
            Enemy(
                self.ENEMY0_START_POS[0],
                self.ENEMY0_START_POS[1],
                0,
                0,
                self.enemy_image_path,
                speed,
                self.OBJECT_SCALE_FACTOR
            ),
            Enemy(
                self.ENEMY1_START_POS[0],
                self.ENEMY1_START_POS[1],
                0,
                0,
                self.enemy_image_path,
                speed,
                self.OBJECT_SCALE_FACTOR
            ),
            Enemy(
                self.ENEMY2_START_POS[0],
                self.ENEMY2_START_POS[1],
                0,
                0,
                self.enemy_image_path,
                speed,
                self.OBJECT_SCALE_FACTOR
            )
        ]
        enemies = []
        for e in range(0, index):
            enemies.append(max_enemies[e])
        return enemies

    def update_display(self):
        self.game_window.fill(self.black_colour)
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for e in range(len(self.enemies)):
            self.game_window.blit(self.enemies[e].image, (self.enemies[e].x, self.enemies[e].y))

        pygame.display.update()

    def move_objects(self, player_direction_x, player_direction_y):
        self.player.move(player_direction_x, player_direction_y,
                         self.X_BOUNDS[0], self.X_BOUNDS[1],
                         self.current_display_size[1])

        for e in range(len(self.enemies)):
            self.enemies[e].move(self.X_BOUNDS)

    def check_collision(self):
        for e in self.enemies:
            if self.detect_collision(self.player, e):
                self.level = 1.0
                return True

        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False

    def detect_collision(self, object_1, object_2):
        if (object_1.y < (object_2.y + object_2.height) and
                (object_1.y + object_1.height) > object_2.y and
                object_1.x < (object_2.x + object_2.width) and
                (object_1.x + object_1.width) > object_2.x):
            return True
        return False

    def run_game_loop(self):
        player_direction_x = 0
        player_direction_y = 0

        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player_direction_y = -1
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player_direction_y = 1
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player_direction_x = -1
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player_direction_x = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player_direction_y = 0
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player_direction_y = 0
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player_direction_x = 0
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player_direction_x = 0

            # Execute logic
            self.move_objects(player_direction_x, player_direction_y)

            # Update display
            self.update_display()

            # Detect collision
            if self.check_collision():
                self.reset_map()

    # since it's not to clear how to get delta-time, I hope this fixed tick-value will solve potential framerate issues
            self.clock.tick(60)
