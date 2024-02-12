import pygame
import random
import sys

from map import Map
from constants import *

tile_cache = {}

def get_tile(tile_x, tile_y):
  """Extracts and returns a single tile from the tileset, using caching."""
  cache_key = (tile_x, tile_y)

  if cache_key in tile_cache:
    return tile_cache[cache_key]

  tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
  tile.blit(tileset, (0, 0), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
  tile_cache[cache_key] = tile
  return tile

def draw_tile(screen, x, y, tile_index):
  """Draws a single tile on the screen."""
  screen.blit(get_tile(tile_index % TILESET_WIDTH, tile_index // TILESET_WIDTH), (x * TILE_SIZE, y * TILE_SIZE))

def draw_grid(screen, map):
  """Draws the entire grid on the screen."""
  screen.fill(pygame.Color('black'))
  for col in range(0, GRID_SIZE + 2):
    for line in range(0, GRID_SIZE + 2):
      # TODO: make this better
      if map.state == 'loosed':
        if map.grid[col][line].value == Tile.MINE:
          if flashing_bomb:
            draw_tile(screen, line, col, Tile.MINE_EXPLODED.value)
          else:
            draw_tile(screen, line, col, Tile.MINE.value)
        else:
          draw_tile(screen, line, col, map.grid[col][line].value.value)
      elif map.state == 'won':
        draw_tile(screen, line, col, map.grid[col][line].value.value)
      else:
        if map.grid[col][line].state == TileState.DISCOVERED:
          draw_tile(screen, line, col, map.grid[col][line].value.value)
        elif map.grid[col][line].state == TileState.FLAGGED:
          draw_tile(screen, line, col, Tile.FLAG.value)
        elif map.grid[col][line].state == TileState.QUESTION:
          draw_tile(screen, line, col, Tile.QUESTION.value)
        else:
          draw_tile(screen, line, col, Tile.UNKNOWN.value)

def main():
  global tileset, flashing_bomb

  random.seed(SEED)
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
  clock = pygame.time.Clock()
  tileset = pygame.image.load('tileset.png').convert_alpha()
  tileset = pygame.transform.scale(tileset, (TILESET_WIDTH * TILE_SIZE, TILESET_HEIGHT * TILE_SIZE))
  map = Map(GRID_SIZE, 15)

  # Timer setup
  FLASHING_BOMB_EVENT = pygame.USEREVENT + 1
  pygame.time.set_timer(FLASHING_BOMB_EVENT, 1000)
  flashing_bomb = False

  running = True
  while running:
    draw_grid(screen, map)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          x, y = pygame.mouse.get_pos()
          map.discover_tile(x, y)
        elif event.button == 3:
          x, y = pygame.mouse.get_pos()
          map.toggle_flag(x, y)
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          map.reset()
      elif event.type == FLASHING_BOMB_EVENT:
        flashing_bomb = not flashing_bomb

    pygame.display.update()

if __name__ == "__main__":
  main()
