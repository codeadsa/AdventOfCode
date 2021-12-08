from typing import List
import numpy as np
tot_count = 0

def parse_file(path: str) -> List[int]:
    with open(path) as f:
        data = f.readlines()
        return data


def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]


long_data = parse_file("./Day08_input.txt") #acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
for data in long_data:
    data = data.strip()
    mapping = [0,0,0,0,0,0,0,0,0,0]
    sixes = []
    five = []
    for signal in data.split("| ")[0].split(" "):
            # map the known numbers
            signal = ''.join(sorted(signal.strip()))
            if len(signal) == 2:
                mapping[1] = signal
            if len(signal) == 4:
                mapping[4] = signal
            if len(signal) == 3:
                mapping[7] = signal
            if len(signal) == 7:
                mapping[8] = signal
            #map the similar in length numbers
            if len(signal) == 6:
                sixes.append(signal)
            if len(signal) == 5:
                five.append(signal)

    #six is missing 1
    for num in sixes:
        if not containsAll(num, set(mapping[1])):
            mapping[6] = num
            sixes.remove(num)
            break

    #nine contains 4
    for num in sixes:
        if containsAll(num, set(mapping[4])):
            mapping[9] = num
            sixes.remove(num)
            break

    #last one has to be 0 then.
    mapping[0] = sixes[0]

    diff_between_8_and_6 = set(mapping[8]) - set(mapping[6])
    diff_between_8_and_6 = diff_between_8_and_6.pop()

    #out of all the length 5, 3 is the only one that contains 1
    for num in five:
        if containsAll(num, set(mapping[1])):
            mapping[3] = num
            five.remove(num)
            break
    #2 has the missing top right (diff between 8 and 6)
    if diff_between_8_and_6 in five[0]:
        mapping[2] = five[0]
        mapping[5] = five[1]
    else:
        mapping[2] = five[1]
        mapping[5] = five[0]

    result = ""
    for answer in data.split("| ")[1].split(" "):
        answer = ''.join(sorted(answer))
        result += str(mapping.index(answer))
    print(result)
    tot_count += int(result)

print(tot_count) #less than 1025568