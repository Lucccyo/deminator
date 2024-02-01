from enum import Enum

# Grid generation
SEED = 19
GRID_SIZE = 10

# Graphical constants
BLOCK_SIZE = 27
INNER_BLOCK_SIZE = BLOCK_SIZE - 2
SCREEN_SIZE = (GRID_SIZE + 2) * BLOCK_SIZE

# Cell values enum ()
class CellValue(Enum):
  EMPTY = 0
  MINE = 9
  FLAG = 10
  QUESTION = 11