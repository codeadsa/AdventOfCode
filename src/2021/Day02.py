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

horiz, depth, aim =0, 0, 0
with open('Day02_input.txt') as f:
    cmds = [(cmd, int(amt)) for cmd, amt in [line.strip().split() for line in f]]
    for cmd, x in cmds:
        if cmd == "down":
            aim += x
        elif cmd == "forward":
            horiz += x
            depth += aim * x
        else:
            aim -= x
print(f'Part2: answer = {horiz * depth}') #1251263225

