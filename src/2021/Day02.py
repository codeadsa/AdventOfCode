from typing import List


def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data

x, y = 0, 0
dataset = parse_file('Day02_input.txt')
for data in dataset:
    if data.startswith("down"):
        y += int(data[5:])
    elif data.startswith("forward"):
        x += int(data[8:])
    else:
        y -= int(data[3:])
print(f'Part1: {x * y}') #1580000

x, y, aim =0, 0, 0
dataset = parse_file('Day02_input.txt')
for data in dataset:
    if data.startswith("down"):
        aim += int(data[5:])
    elif data.startswith("forward"):
        x += int(data[8:])
        y += aim * int(data[8:])
    else:
        aim -= int(data[3:])
print(f'Part2: answer = {x * y}') #1251263225

