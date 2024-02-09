from constants import *

class Cell:
  discovered = False
  value = Tile.EMPTY

  def __init__(self, value, discovered = False):
    self.discovered = discovered
    self.value = value
