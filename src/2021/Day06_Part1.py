from typing import List
import numpy as np

def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data

def next_day():
    updated_fishes = []
    new_fishes = []

    for  fish in fishes:
        if fish != 0:
            fish -= 1
            updated_fishes.append(fish)
        else:
            updated_fishes.append(6)
            new_fishes.append(8)

    updated_fishes = updated_fishes + new_fishes
    return updated_fishes


days = None
with open("./Day06_sample.txt") as f:
    fishes = [line.strip().split(',') for line in f]
    fishes = [int(num) for num in fishes[0]]

days_to_run = 256
while days_to_run > 0:
    days_to_run -=1
    fishes = next_day()

print(f'Part1 {len(fishes)}') #372984