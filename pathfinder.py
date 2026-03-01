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
