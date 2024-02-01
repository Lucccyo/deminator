import pygame
import random
import math

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

def create_map(size):
    map = []
    for i in range(0, size):
        width  = random.randint(math.floor(size/2) + 1, size)
        offset = random.randint(0, math.floor(size/2) - 1)
        line = []
        for j in range(0, size):
            if (j < offset or j > width + offset):
                line.append(' ')
            else:
                line.append('0')
        line.insert(0,' ')
        line.append(' ')
        map.append(line)
    map.insert(0, [' '] * (size + 2))
    map.append([' '] * (size + 2))
    return map

def is_number(map, l, c):
    return l >= 0 and l < len(map) and map[l][c] != ' ' and map[l][c] != '+'

def incr_neigbours(map, l, c):
    if (is_number(map, l-1, c-1)):
        map[l-1][c-1] = chr(ord(map[l-1][c-1]) + 1)
    if (is_number(map, l-1, c)):
        map[l-1][c] = chr(ord(map[l-1][c]) + 1)
    if (is_number(map, l-1, c+1)):
        map[l-1][c+1] = chr(ord(map[l-1][c+1]) + 1)
    if (is_number(map, l, c-1)):
        map[l][c-1] = chr(ord(map[l][c-1]) + 1)
    if (is_number(map, l, c+1)):
        map[l][c+1] = chr(ord(map[l][c+1]) + 1)
    if (is_number(map, l+1, c-1)):
        map[l+1][c-1] = chr(ord(map[l+1][c-1]) + 1)
    if (is_number(map, l+1, c)):
        map[l+1][c] = chr(ord(map[l+1][c]) + 1)
    if (is_number(map, l+1, c+1)):
        map[l+1][c+1] = chr(ord(map[l+1][c+1]) + 1)
    return map


def add_mines(map, n):
    empty_coords = False
    for i in range(0, n):
        l = 0
        c = 0
        while not empty_coords:
            l = random.randint(0, len(map) - 1)
            c = random.randint(0, len(map) - 1)
            i = ord(map[l][c])
            empty_coords = (i >= 48 and i <= 57)
        map[l][c] = '+'
        map = incr_neigbours(map, l, c)
        empty_coords = False
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
            # match map[line][col]:
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

    map = create_map(size)
    map = add_mines(map, 16)
    print_map(map)
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

