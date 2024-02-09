import random
import math

from cell import Cell
from constants import *
class Map:
  def __init__(self, size, mines):
    self.size = size
    self.mines = mines
    self.grid = []
    self.create_square_map()

  def create_square_map(self):
    """Creates a square map with the given size and number of mines, surrounded by walls."""
    self.grid = [[Cell(Tile.WALL, True) if i == 0 or i == self.size + 1 or j == 0 or j == self.size + 1 else Cell(Tile.EMPTY) for j in range(self.size + 2)] for i in range(self.size + 2)]

    available_positions = [(i, j) for i in range(1, self.size + 1) for j in range(1, self.size + 1)]

    if len(available_positions) < self.mines:
      raise Exception('Not enough available positions for mines')

    for _ in range(self.mines):
      pos = random.choice(available_positions)
      x, y = pos
      self.grid[x][y].value = Tile.MINE
      self.incr_neighbours(x, y)
      available_positions.remove(pos)

  def create_random_map(self):
    for i in range(0, self.size):
      width  = random.randint(math.floor(self.size / 2) + 1, self.size)
      offset = random.randint(0, math.floor(self.size / 2) - 1)
      line = []
      for j in range(0, self.size):
        if (j < offset or j > width + offset):
          line.append(Cell(Tile.WALL, True))
        else:
           line.append(Cell(Tile.EMPTY))
      line.insert(0, Cell(Tile.WALL, True))
      line.append(Cell(Tile.WALL, True))
      self.grid.append(line)
    self.grid.insert(0, [Cell(Tile.WALL, True)] * (self.size + 2))
    self.grid.append([Cell(Tile.WALL, True)] * (self.size + 2))

    available_positions = [(i, j) for i in range(1, self.size + 1) for j in range(1, self.size + 1)]

    if len(available_positions) < self.mines:
      raise Exception('Not enough available positions for mines')

    for _ in range(self.mines):
      pos = random.choice(available_positions)
      x, y = pos
      self.grid[x][y].value = Tile.MINE
      self.incr_neighbours(x, y)
      available_positions.remove(pos)

  def incr_neighbours(self, x, y):
    """Increments the value of the neighbours of the given cell."""
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        nx, ny = x + i, y + j
        if 0 < nx < self.size + 1 and 0 < ny < self.size + 1:
          neighbor = self.grid[nx][ny]
          if neighbor.value != Tile.WALL and neighbor.value != Tile.MINE:
            neighbor.value = Tile(neighbor.value.value + 1)

  def __str__(self):
    result = ''
    for line in self.grid:
      for cell in line:
        char = str(cell.value.value) if cell.discovered else "X"
        result += char + ' '
      result += '\n'
    return result

if __name__ == "__main__":
  map = Map(20, 40)
  print(map)