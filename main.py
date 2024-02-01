import pygame
import random

from map import Map
from constants import *

def create_square_map(size):
    map = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append('0')
        line.insert(0,' ')
        line.append(' ')
        map.append(line)
    map.insert(0, [' '] * (size + 2))
    map.append([' '] * (size + 2))
    return map

def fill_cell(screen, x, y, color):
  r = pygame.Rect(BLOCK_SIZE * x, BLOCK_SIZE * y, INNER_BLOCK_SIZE, INNER_BLOCK_SIZE)
  pygame.draw.rect(screen, color, r)

def drawGrid(screen, map):
    screen.fill(pygame.Color('black'))
    for x in range(0, SCREEN_SIZE, BLOCK_SIZE):
        for y in range(0, SCREEN_SIZE, BLOCK_SIZE):
            color = pygame.Color('grey')
            line = int(y / BLOCK_SIZE)
            col  = int(x / BLOCK_SIZE)
            match map.grid[line][col]:
              case ' ':
                color = pygame.Color('black')
              case '+':
                color = pygame.Color('red')
              case _:
                if not (map.grid[line][col] == '0'):
                  rgb = int(map.grid[line][col]) / 8 * 255
                  color = (rgb, rgb, rgb)
            fill_cell(screen, col, line, color)

def main():
    random.seed(SEED)
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
    clock = pygame.time.Clock()

    map = Map(GRID_SIZE, 15)
    print(map)
    running = True
    while running:
        drawGrid(screen, map)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
  main()
