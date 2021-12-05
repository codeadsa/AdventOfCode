from typing import List
import numpy as np

def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data


def init_boards():
    boards = []

    i = 1
    while i < len(data):
        if len(data[i].strip()) == 0:
            i += 1
            board = []
            for j in range(5):
                board.append([int(num) for num in data[i + j].replace("  ", " ").strip().split(" ")])
            boards.append(board)
        i += 5
    return boards

def board_match(num):
    for i in range(len(boards)):
        board = boards[i]
        for j in range(len(board)):
            line = board[j]
            line = np.array(line)
            line = list(np.where(line == num, -1, line))
            board[j] = line

def is_this_board_bingo(board):
    for j in range(len(board)):
        line = board[j]
        if sum(line) == -5:
            return board

    # transpose the board make vertical now horiz, and do same check
    transboard = np.transpose(board)
    for j in range(len(transboard)):
        line = transboard[j]
        if sum(line) == -5:
            return board
    return None


def is_bingo():
    for i in range(len(boards)):
        board = boards[i]
        if is_this_board_bingo(board) is not None:
            return board
    return None


def get_sum_of_bingo_board(board):
    board_sum = 0

    for j in range(len(board)):
        line = board[j]
        line = np.array(line)
        line = list(np.where(line == -1, 0, line))
        board[j] = line
        board_sum += sum(line)
    return board_sum


def part1():
    for num in picked_nums:
        board_match(num)
        bingo_board = is_bingo()
        if bingo_board is not None:
            sum = get_sum_of_bingo_board(bingo_board)
            print(f'Part1 - Sum:{sum}, num:{num}, ans ={sum * num}')  # 4512, 55770
            break

def part2():

    board_sum = 0
    count = 0
    called_num = []
    solved_idx = []
    while len(boards):
        for num in picked_nums:

            board_match(num)

            for idx, board in enumerate(boards):
                if idx in solved_idx:
                    if len(solved_idx) == 100:
                        break;
                    continue

                if is_this_board_bingo(board):
                    sum = get_sum_of_bingo_board(board)
                    called_num.append(sum * num)
                    solved_idx.append(idx)
                    count += 1
                    print(f'Board idx {idx} removed {count} {board}, sum={sum} num={num}')

    print(called_num[-1])

def part2b():

    board_sum = 0
    count = 0
    called_num = []
    while len(boards):
        for num in picked_nums:

            board_match(num)
            #
            # if len(boards) == 1:
            #     board = boards[0]
            #     if is_this_board_bingo(board) is None:
            #         continue
            #     else:
            #         board_sum = get_sum_of_bingo_board(board)
            #         print(f'Part2 - Sum:{board_sum}, num:{num}, ans ={board_sum * num}')  #1924, NOT 1368
            #         break;
            for idx, board in enumerate(boards):
                if is_this_board_bingo(board):
                    sum = get_sum_of_bingo_board(board)
                    called_num.append(sum * num)
                    boards.remove(board)
                    count += 1
                    print(f'Board idx {idx} removed {count} {board}, sum={sum} num={num}')

    print(called_num[0])

data = parse_file("./Day04_input.txt")
picked_nums = ([int(num) for num in data[0].split(",")])
boards = init_boards()

#part1()
part2()
