import pygame
import random
import math

from map import Map

seed = 19
size = 10
block_size = 27
inner_block = block_size - 2
black = (0, 0, 0) # wall
red = (200, 0, 0) # mine
grey = (100, 100, 100)  # number
screen_size = (size * block_size) + 2
random.seed(seed)
pygame.init()

def print_map(tab):
    for line in tab:
        print(' '.join(line))

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
  r = pygame.Rect(block_size*x + 1, block_size*y + 1, inner_block, inner_block)
  pygame.draw.rect(screen, color, r)

def drawGrid(screen, map):
    screen.fill(black)
    for x in range(0, screen_size, block_size):
        for y in range(0, screen_size, block_size):
            color = grey
            line = int(x / block_size)
            col  = int(y / block_size)
            # match map.grid[line][col]:
            #     case ' ':
            #         color = black
            #         break;
            #     case '+':
            #         color = red
            #         break;
            #     case _:
            #         break;
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, color, rect, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_size, screen_size])
    clock = pygame.time.Clock()

    map = Map(size, 40)
    running = True
    while running:
        drawGrid(screen, map)
        fill_cell(screen, 0, 0, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()

