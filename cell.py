from constants import *

class Cell:
  discovered = TileState.UNDISCOVERED
  value = Tile.EMPTY

  def __init__(self, value, discovered = TileState.UNDISCOVERED):
    self.state = discovered
    self.value = value
