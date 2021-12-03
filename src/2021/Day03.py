from typing import List


def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
gama, epsi = "", ""

data = parse_file("Day03_input.txt")
for line in data:
    for i in range (len(line) -1):
        if line[i] == '1':
            ones[i] += 1

threshold = len(data) / 2

for i in range (len(ones)):
    if ones[i] > threshold:
        gama += "1"
        epsi += "0"
    else:
        gama += "0"
        epsi += "1"

print(f"Part 1 {int(gama, 2) * int(epsi, 2)}") #1092896


def num_of_ones_in_position(pos:int, data) -> int:
    ones_counter = 0;
    for line in data:
        if line[pos] == "1":
            ones_counter += 1
    return ones_counter


data = parse_file("Day03_input.txt")
most,least = "",""
threshold = len(data) / 2
line_size = 12
for i in range (line_size):
    ones_count = num_of_ones_in_position(i, data)
    if ones_count > threshold:
        most += "1"
    elif ones_count == threshold:
        most += "1"
    else:
        most += "0"
    data = [x for x in data if x.startswith(most)]
    threshold = len(data) / 2

    if len(data) == 1:
        least = data[0]
        break
print(f'most = {most}')
print(int(most,2))

data = parse_file("Day03_input.txt")
least = ""
threshold = len(data) / 2
for i in range (line_size):
    ones_count = num_of_ones_in_position(i, data)
    if ones_count > threshold:
        least += "0"
    elif ones_count == threshold:
        least += "0"
    else:
        least += "1"
    data = [x for x in data if x.startswith(least)]
    threshold = len(data) / 2

    if len(data) == 1:
        least = data[0]
        break
print(f'least = {least}')
print(int(least,2))

print(int(most,2) * int(least,2)) #4672151