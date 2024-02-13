from constants import *

def solve(map):
  """Return a position and an action to take."""
  pos = discover_free_tile(map)
  if pos != None:
    return (pos, 'discover')

  pos = flag_free_tile(map)
  if pos != None:
    return (pos, 'flag')


def check_neighbors_flagged(map, x, y):
  """Return the amount of neighbors that are flagged."""
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if map.grid[x + i][y + j].state == TileState.FLAGGED:
        count += 1
  return count

def check_neighbors_unknown(map, x, y):
  """Return the amount of neighbors that are unknown."""
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if map.grid[x + i][y + j].state == TileState.UNDISCOVERED:
        count += 1
  return count

def discover_free_tile(map):
  """
  Return a position to discover.

  If a tile is discovered and has the same amount of flagged neighbors as its
  value, then discover the unknown neighbors.
  """
  for i in range(1, map.size + 1):
    for j in range(1, map.size + 1):
      if map.grid[i][j].state == TileState.DISCOVERED and map.grid[i][j].value != Tile.EMPTY:
        if check_neighbors_flagged(map, i, j) == map.grid[i][j].value.value:
          for k in range(-1, 2):
            for l in range(-1, 2):
              if map.grid[i + k][j + l].state == TileState.UNDISCOVERED:
                return (i + k, j + l)
  return None

def flag_free_tile(map):
  """
  Return a position to flag.

  If a tile is discovered and has the same amount of unknown neighbors as its
  value minus the amount of flagged neighbors, then flag the unknown neighbors.
  """
  for i in range(1, map.size + 1):
    for j in range(1, map.size + 1):
      if map.grid[i][j].state == TileState.DISCOVERED and map.grid[i][j].value != Tile.EMPTY:
        if check_neighbors_unknown(map, i, j) == map.grid[i][j].value.value - check_neighbors_flagged(map, i, j):
          for k in range(-1, 2):
            for l in range(-1, 2):
              if map.grid[i + k][j + l].state == TileState.UNDISCOVERED:
                return (i + k, j + l)
  return None