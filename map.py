import random
import math

class Map:
  def __init__(self, size, mines):
    self.grid = []
    self.size = size
    self.mines = mines

    self.create_random_map()

  def create_random_map(self):
    for i in range(0, self.size):
      width  = random.randint(math.floor(self.size/2) + 1, self.size)
      offset = random.randint(0, math.floor(self.size/2) - 1)
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

    empty_coords = False
    for i in range(self.mines):
      l, c = 0, 0
      while not empty_coords:
        l = random.randint(0, len(self.grid) - 1)
        c = random.randint(0, len(self.grid[l]) - 1)
        i = ord(self.grid[l][c])
        empty_coords = (i >= 48 and i <= 57)
      self.grid[l][c] = '+'
      self.incr_neighbours(l, c)
      empty_coords = False

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