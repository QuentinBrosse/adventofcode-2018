#!/usr/bin/env python3

import os
import re
from collections import defaultdict
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))
inputPath = os.path.join(cwd, "input.txt")

def puzzle1(inches):
    return len(list(filter(lambda x: x[1] >= 2 , inches.items())))

def puzzle2(lines, inches):    
    for id, x, y, width, height in lines:
        iterations = 0
        overlap_sum = 0
        for cx in range(x, x + width):
            for cy in range (y, y + height):
                c = "{}x{}".format(cx, cy)
                iterations += 1
                overlap_sum += inches[c]
        if iterations == overlap_sum:
            return id
    return -1

def prepare():
    lines = []
    inches = defaultdict(int)
    rgx = re.compile("#([\d]+) @ (\d+),(\d+): (\d+)x(\d+)")
    with open(inputPath, "r") as f:
        for line in f:
            id, x, y, width, height = rgx.findall(line)[0]
            x = int(x) + 1
            y = int(y) + 1
            width = int(width)
            height = int(height)

            lines.append((id, x, y, width, height))
            for cx in range(x, x + width):
                for cy in range (y, y + height):
                    c = "{}x{}".format(cx, cy)
                    inches[c] += 1
    return lines, inches

if __name__ == "__main__":
    lines, inches = prepare()
    
    print("Rep 1: {}".format(puzzle1(inches)))
    print("Rep 2: {}".format(puzzle2(lines, inches)))
