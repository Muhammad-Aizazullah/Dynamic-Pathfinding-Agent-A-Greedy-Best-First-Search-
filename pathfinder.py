import pygame, random, time, heapq
pygame.init()

WIDTH = 600
ROWS = 25
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Dynamic Pathfinding Agent")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PATH_COLOR = (0,200,0)
GREY = (200,200,200)

DYNAMIC_MODE = False
ALGO = "A*"
MODE = None

font = pygame.font.SysFont("arial", 18)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.label = ""

    def get_pos(self):
        return self.row, self.col

    def is_barrier(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE
        self.label = ""

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def make_start(self):
        self.color = GREEN
        self.label = "S"

    def make_end(self):
        self.color = RED
        self.label = "G"
if MODE == "START":
    if start is None and node not in ends:
        start = node
        start.make_start()
    MODE = None

elif MODE == "GOAL":
    if node != start and node not in ends:
        node.make_end()
        ends.append(node)
    MODE = None

else:
    if node != start and node not in ends:
        node.make_barrier()

elif pygame.mouse.get_pressed()[2]:
    row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, width)
    node = grid[row][col]
    if node == start:
        start = None
    if node in ends:
        ends.remove(node)
    node.reset()

if event.key == pygame.K_1:
    ALGO = "A*"
    print("Algorithm: A*")

if event.key == pygame.K_2:
    ALGO = "GBFS"
    print("Algorithm: Greedy Best First")

if event.key == pygame.K_SPACE and start and len(ends) > 0:
    MODE = None
    for row in grid:
        for node in row:
            node.update_neighbors(grid)
    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, ends)

def reconstruct_path(came_from, current, draw):
    cost = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        cost += 1
        draw()
    return cost
if DYNAMIC_MODE and random.random() < 0.02:
    r = random.randint(0, ROWS-1)
    c = random.randint(0, ROWS-1)
    node = grid[r][c]
    if node != start and node not in ends:
        node.make_barrier()
        for row in grid:
            for n in row:
                n.update_neighbors(grid)
