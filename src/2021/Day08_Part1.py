from typing import List
import numpy as np

def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data


data = parse_file("Day08_input.txt")
count = 0
for idx, signal in enumerate(data):
        sigs = signal = signal.strip().split("| ")[1].split(" ")
        for sig in sigs:
            if len(sig) != 5 and len(sig) != 6:
                count += 1
print(count) # 237