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

    def make_start(self):
        self.color = GREEN
        self.label = "S"

    def make_end(self):
        self.color = RED
        self.label = "G"

    def make_barrier(self):
        self.color = BLACK
        self.label = ""

    def make_open(self):
        self.color = YELLOW

    def make_closed(self):
        self.color = BLUE

    def make_path(self):
        self.color = PATH_COLOR

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        if self.label != "":
            text = font.render(self.label, True, BLACK)
            win.blit(text, (self.x + self.width//3, self.y + self.width//4))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])

def h(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def reconstruct_path(came_from, current, draw):
    cost = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        cost += 1
        draw()
    return cost

def algorithm(draw, grid, start, ends):
    start_time = time.time()
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    open_set_hash = {start}
    visited = 0

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)
        visited += 1

        if current in ends:
            path_cost = reconstruct_path(came_from, current, draw)
            end_time = time.time()
            print("Nodes Visited:", visited)
            print("Path Cost:", path_cost)
            print("Execution Time(ms):", round((end_time-start_time)*1000,2))
            return True

        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                if ALGO == "A*":
                    f_score[neighbor] = temp_g + min(h(neighbor.get_pos(), e.get_pos()) for e in ends)
                else:
                    f_score[neighbor] = min(h(neighbor.get_pos(), e.get_pos()) for e in ends)
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

        if DYNAMIC_MODE and random.random() < 0.02:
            r = random.randint(0, ROWS-1)
            c = random.randint(0, ROWS-1)
            node = grid[r][c]
            if node != start and node not in ends:
                node.make_barrier()
                for row in grid:
                    for n in row:
                        n.update_neighbors(grid)

    return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Node(i, j, gap, rows))
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    global DYNAMIC_MODE, ALGO, MODE
    grid = make_grid(ROWS, width)
    start = None
    ends = []
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, width)
                node = grid[row][col]

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    MODE = "START"

                if event.key == pygame.K_g:
                    MODE = "GOAL"

                if event.key == pygame.K_c:
                    MODE = None
                    start = None
                    ends = []
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_r:
                    for row in grid:
                        for node in row:
                            if random.random() < 0.3:
                                node.make_barrier()

                if event.key == pygame.K_1:
                    ALGO = "A*"
                    print("Algorithm: A*")

                if event.key == pygame.K_2:
                    ALGO = "GBFS"
                    print("Algorithm: Greedy Best First")

                if event.key == pygame.K_d:
                    DYNAMIC_MODE = not DYNAMIC_MODE
                    print("Dynamic Mode:", DYNAMIC_MODE)

                if event.key == pygame.K_SPACE and start and len(ends) > 0:
                    MODE = None
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, ends)

    pygame.quit()

main(win, WIDTH)
