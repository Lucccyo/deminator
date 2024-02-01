import random
import math

class Map:
  grid = []

  def __init__(self, size, mines):
    self.size = size
    self.mines = mines
    self.create_random_map()

  def create_random_map(self):
    for i in range(0, self.size):
      width  = random.randint(math.floor(self.size / 2) + 1, self.size)
      offset = random.randint(0, math.floor(self.size / 2) - 1)
      line = []
      for j in range(0, self.size):
        if (j < offset or j > width + offset):
          line.append(' ')
        else:
          line.append('0')
      line.insert(0, ' ')
      line.append(' ')
      self.grid.append(line)
    self.grid.insert(0, [' '] * (self.size + 2))
    self.grid.append([' '] * (self.size + 2))

    available_positions = []
    for i in range(1, self.size + 1):
      for j in range(1, self.size + 1):
        if (self.grid[i][j] == '0'):
          available_positions.append((i, j))

    if (len(available_positions) < self.mines):
      raise Exception('Not enough available positions for mines')

    for i in range(0, self.mines):
      pos = random.randint(0, len(available_positions) - 1)
      x, y = available_positions[pos]
      self.grid[x][y] = '+'
      self.incr_neighbours(x, y)
      del available_positions[pos]

  def incr_neighbours(self, x, y):
    for i in range(-1, 2):
      for j in range(-1, 2):
        if (i == 0 and j == 0):
          continue
        l, c = x + i, y + j
        if l >= 0 and l < len(self.grid) and self.grid[l][c] != ' ' and self.grid[l][c] != '+':
          self.grid[x+i][y+j] = chr(ord(self.grid[x+i][y+j]) + 1)

  def __str__(self) -> str:
    return '\n'.join([' '.join(line) for line in self.grid])

if __name__ == "__main__":
  map = Map(20, 40)
  print(map)