import random
import math

seed = 19
random.seed(seed)

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

map = create_map(10)
map = add_mines(map, 16) # add 16 mines to the 
print_map(map)

