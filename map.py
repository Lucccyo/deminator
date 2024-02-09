import random
import math

from constants import *

class Map:
  grid = []

  def __init__(self, size, mines):
    self.size = size
    self.mines = mines
    self.create_random_map()

  def create_square_map(self):
    """Creates a square map with the given size and number of mines."""
    self.grid.append([Tile.WALL] * (self.size + 2))
    for i in range(0, self.size):
      line = []
      line.append(Tile.WALL)
      for j in range(0, self.size):
        line.append(Tile.EMPTY)
      line.append(Tile.WALL)
      self.grid.append(line)
    self.grid.append([Tile.WALL] * (self.size + 2))

    available_positions = []
    for i in range(1, self.size + 1):
      for j in range(1, self.size + 1):
        available_positions.append((i, j))

    if (len(available_positions) < self.mines):
      raise Exception('Not enough available positions for mines')

    for i in range(0, self.mines):
      pos = random.randint(0, len(available_positions) - 1)
      x, y = available_positions[pos]
      self.grid[x][y] = Tile.MINE
      self.incr_neighbours(x, y)
      del available_positions[pos]

  def create_random_map(self):
    """Creates a random map with the given size and number of mines."""
    for i in range(0, self.size):
      width  = random.randint(math.floor(self.size / 2) + 1, self.size)
      offset = random.randint(0, math.floor(self.size / 2) - 1)
      line = []
      for j in range(0, self.size):
        if (j < offset or j > width + offset):
          line.append(Tile.WALL)
        else:
          line.append(Tile.EMPTY)
      line.insert(0, Tile.WALL)
      line.append(Tile.WALL)
      self.grid.append(line)
    self.grid.insert(0, [Tile.WALL] * (self.size + 2))
    self.grid.append([Tile.WALL] * (self.size + 2))

    available_positions = []
    for i in range(1, self.size + 1):
      for j in range(1, self.size + 1):
        if (self.grid[i][j] == Tile.EMPTY):
          available_positions.append((i, j))

    if (len(available_positions) < self.mines):
      raise Exception('Not enough available positions for mines')

    for i in range(0, self.mines):
      pos = random.randint(0, len(available_positions) - 1)
      x, y = available_positions[pos]
      self.grid[x][y] = Tile.MINE
      self.incr_neighbours(x, y)
      del available_positions[pos]

  def incr_neighbours(self, x, y):
    """Increments the value of the neighbours of the given cell."""
    for i in range(-1, 2):
      for j in range(-1, 2):
        if (i == 0 and j == 0):
          continue
        l, c = x + i, y + j
        if l >= 0 and l < len(self.grid) and self.grid[l][c] != Tile.WALL and self.grid[l][c] != Tile.MINE:
          self.grid[x+i][y+j] = Tile(self.grid[l][c].value + 1)

  def __str__(self) -> str:
    result = ''
    for line in self.grid:
      for cell in line:
        result += str(cell.value) + ' '
      result += '\n'
    return result

if __name__ == "__main__":
  map = Map(20, 40)
  print(map)