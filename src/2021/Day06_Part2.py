from typing import List
import numpy as np

with open("./Day06_input.txt") as f:
    fishes = [line.strip().split(',') for line in f]
    fishes = [int(num) for num in fishes[0]]

eight_counter = [0,0,0,0,0,0,0,0,0]

#init
for cycle in fishes:
    eight_counter[cycle] += 1

for i in range(256):

    tmp_eightth_counter = eight_counter[8]
    eight_counter[8] = eight_counter[0]
    eight_counter[7] += eight_counter[0]
    for i in range (0,8):
        eight_counter[i] = eight_counter[i+1]
    eight_counter[7] = tmp_eightth_counter

print(sum(eight_counter)) #1681503251694