import random
from os import path

# Window Settings
HEIGHT = 600
WIDTH = 900
GAME_WIDTH = 600
GAME_HEIGHT = 600
FPS = 60

game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder, "img")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (255, 0, 255)

# Coordinates
COORDINATES = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
RANDOM_COORDINATE = COORDINATES[random.randrange(-1, 12)]
USED_COORDS = []

