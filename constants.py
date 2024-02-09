from enum import Enum

# Grid generation
SEED = 20
GRID_SIZE = 10

# Tileset constants
TILE_SIZE = 32
TILESET_WIDTH = 4
TILESET_HEIGHT = 5

# Graphical constants
SCREEN_SIZE = (GRID_SIZE + 2) * TILE_SIZE

# Game constants
class Tile(Enum):
  EMPTY = 0
  NUMBER_1 = 1
  NUMBER_2 = 2
  NUMBER_3 = 3
  NUMBER_4 = 4
  NUMBER_5 = 5
  NUMBER_6 = 6
  NUMBER_7 = 7
  NUMBER_8 = 8
  MINE = 9
  MINE_EXPLODED = 10
  UNKNOWN = 11
  FLAG = 12
  WALL = 13