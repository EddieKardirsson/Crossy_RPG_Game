import pygame
from game import Game

pygame.init()

resolution_4k = (3840, 2160)
resolution_2k = (2560, 1440)
resolution_1080p = (1920, 1080)
resolution_720p = (1280, 720)

game = Game(resolution_2k)
game.run_game_loop()

pygame.quit()
quit()
