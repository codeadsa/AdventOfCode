from typing import List


def parse_file_to_ints(path: str) -> List[int]:
    with open(path) as f:
        data = f.read()
        return [int(l) for l in data.splitlines()]

# Part 1
count = 0
dataset = parse_file_to_ints('Day01_input.txt')
for i in range(len(dataset)-1):
    if dataset[i] < dataset[i+1]:
        count += 1
print (f'Part 1: {count}') #1581

# Part 2
count = 0
dataset = parse_file_to_ints('Day01_input.txt')
for i in range(len(dataset) - 3):
    if sum(dataset[i:i+3]) < sum(dataset[i+1:i+4]):
        count += 1
print (f'Part 2: {count}') #1618

# Part 2 trick
count = 0
dataset = parse_file_to_ints('Day01_input.txt')
for i in range(len(dataset)-3):
    if (dataset[i] < dataset[i+3]):
        count += 1
print (f'Part 2 Trick: {count}') #1618
