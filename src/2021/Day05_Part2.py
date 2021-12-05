from typing import List
import numpy as np

def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data

board = np.empty((999, 999))
board.fill(0)

def parse_line(line):
    line.strip()
    x1 = int(line.split(" -> ")[0].split(",")[0])
    y1 = int(line.split(" -> ")[0].split(",")[1])
    x2 = int(line.split(" -> ")[1].split(",")[0])
    y2 = int(line.split(" -> ")[1].split(",")[1])
    return x1, y1, x2, y2


def add_line(x1,y1,x2,y2):
    if x1 == x2:
        if y2 < y1:
            tmp = y1
            y1 = y2
            y2 = tmp
        for y in range(y1+1, y2):
            board[y][x1] += 1
        board[y1][x1] += 1
        board[y2][x2] += 1
    elif y1 == y2:
        if x2 < x1:
            tmp = x1
            x1 = x2
            x2 = tmp
        for x in range(x1+1, x2):
            board[y1][x] += 1
        board[y1][x1] += 1
        board[y2][x2] += 1
    else:
        board[y1][x1] += 1

        dx, dy = 1, 1
        if x1 > x2:
            dx = -1
        if y1 > y2:
            dy = -1
        while x1 != x2 and y1 != y2:
            x1 += dx
            y1 += dy
            board[y1][x1] += 1



def count_board(greater_than):
    return np.count_nonzero(board > greater_than)

data = parse_file("./Day05_input.txt")
for line in data:
    x1,y1,x2,y2 = parse_line(line)
    add_line(x1,y1,x2,y2)
print(f'Number of items 2 or greater = {count_board(1)}')