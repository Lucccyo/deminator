import random
import math

from cell import Cell
from constants import *

class Map:

  def __init__(self, size, mines):
    self.size = size
    self.mines = mines
    self.discovered_neighbours = []
    self.discovered_mines = 0
    self.grid = []
    self.state = 'running'
    self.create_square_map()
    self.discover_first_tile()

  def reset(self):
    self.__init__(self.size, self.mines)

  def create_square_map(self):
    """Creates a square map with the given size and number of mines, surrounded by walls."""
    self.grid = [[Cell(Tile.WALL, TileState.DISCOVERED) if i == 0 or i == self.size + 1 or j == 0 or j == self.size + 1 else Cell(Tile.EMPTY) for j in range(self.size + 2)] for i in range(self.size + 2)]

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
          line.append(Cell(Tile.WALL, TileState.DISCOVERED))
        else:
           line.append(Cell(Tile.EMPTY))
      line.insert(0, Cell(Tile.WALL, TileState.DISCOVERED))
      line.append(Cell(Tile.WALL, TileState.DISCOVERED))
      self.grid.append(line)
    self.grid.insert(0, [Cell(Tile.WALL, TileState.DISCOVERED)] * (self.size + 2))
    self.grid.append([Cell(Tile.WALL, TileState.DISCOVERED)] * (self.size + 2))

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

  def discover_tile(self, x, y):
    """Discover the tile at the given x, y screen coordinates."""
    if 0 <= x < self.size + 2 and 0 <= y < self.size + 2:
      if self.grid[y][x].state == TileState.DISCOVERED:
        self.discover_around(x, y)
        return
      if self.grid[y][x].state == TileState.FLAGGED:
        return
      self.grid[y][x].state = TileState.DISCOVERED
      if self.grid[y][x].value == Tile.MINE:
        self.state = 'loosed';
      elif self.grid[y][x].value == Tile.EMPTY:
        self.discover_neighbours(x, y)
    self.check_win()

  def discover_neighbours(self, x, y):
    """Discover the neighbours of the given cell."""
    if (x, y) in self.discovered_neighbours:
      return
    self.discovered_neighbours.append((x, y))
    for i in range(-1, 2):
      for j in range(-1, 2):
        nx, ny = x + i, y + j
        if 0 < nx < self.size + 1 and 0 < ny < self.size + 1:
          if self.grid[ny][nx].state == TileState.DISCOVERED:
            continue
          self.grid[ny][nx].state = TileState.DISCOVERED
          if self.grid[ny][nx].value == Tile.EMPTY:
            self.discover_neighbours(nx, ny)

  def toggle_flag(self, x, y):
    """Flag the tile at the given x, y screen coordinates."""
    if 0 <= x < self.size + 2 and 0 <= y < self.size + 2:
      if self.grid[y][x].state == TileState.DISCOVERED:
        return
      elif self.grid[y][x].state == TileState.FLAGGED:
        self.grid[y][x].state = TileState.QUESTION
        self.discovered_mines -= 1
      elif self.grid[y][x].state == TileState.QUESTION:
        self.grid[y][x].state = TileState.UNDISCOVERED
      else:
        self.grid[y][x].state = TileState.FLAGGED
        self.discovered_mines += 1
    self.check_win()

  def discover_around(self, x, y):
    """Discover the neighbours of the given cell."""
    if 0 < x < self.size + 1 and 0 < y < self.size + 1:
      for i in range(-1, 2):
        for j in range(-1, 2):
          nx, ny = x + i, y + j
          if self.grid[ny][nx].state == TileState.UNDISCOVERED:
            self.grid[ny][nx].state = TileState.DISCOVERED
            if self.grid[ny][nx].value == Tile.MINE:
              self.state = 'loosed'
    self.check_win()

  def check_win(self):
    """Check if the game is won."""
    if self.discovered_mines == self.mines:
      for i in range(1, self.size + 1):
        for j in range(1, self.size + 1):
          if self.grid[i][j].value == Tile.MINE and self.grid[i][j].state != TileState.FLAGGED or self.grid[i][j].state != TileState.DISCOVERED and self.grid[i][j].value != Tile.MINE:
            return
      self.state = 'won'

  def discover_first_tile(self):
    """Discover the first tile of the game."""
    possible_positions = []
    for i in range(1, self.size + 1):
      for j in range(1, self.size + 1):
        if self.grid[i][j].value == Tile.EMPTY:
          possible_positions.append((i, j))
    x, y = random.choice(possible_positions)
    self.discover_tile(y, x)

  def __str__(self):
    result = ''
    for line in self.grid:
      for cell in line:
        char = str(cell.value.value) if cell.discovered else "X"
        result += char + ' '
      result += '\n'
    return result
