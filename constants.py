from enum import Enum

# Graphical constants
UI_SIZE = 100
SCREEN_SIZE = [660, 660 + UI_SIZE]

# Grid generation
SEED = 20
GRID_SIZE = 20 # TODO: Determine in a menu later
MINE_AMOUNT = 60

# Tileset constants
TILE_SIZE = SCREEN_SIZE[0] // (GRID_SIZE + 2)
TILESET_WIDTH = 4
TILESET_HEIGHT = 5

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
  MINE = 9                # Useless
  MINE_EXPLODED = 10      # Useless
  UNKNOWN = 11            # Useless
  FLAG = 12               # Useless
  WALL = 13
  QUESTION = 14

class TileState(Enum):
  UNDISCOVERED = 0
  DISCOVERED = 1
  FLAGGED = 2
  QUESTION = 3
