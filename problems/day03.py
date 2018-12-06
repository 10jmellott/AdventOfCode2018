""""Day 3: No Matter How You Slice It
https://adventofcode.com/2018/day/3
Part 1: How many square inches of fabric are within two or more claims?
"""

import re

def _load_file():
    # Open the file in read-only mode
    return open('data/day3.txt', 'r')

def _part1():
    """Part 1
    Use regex to parse the input (claims).
    Create a single dimension array for the fabric and go through each claim,
    tallying the claim on the fabric array.
    Finally go through the fabric and check spaces with > 1 claim.
    Returns:
        Integer: Square inches of overlapping fabric
    """
    # Load the input
    f = _load_file()
    # Generate pattern for the input data
    pattern = re.compile('#\\d+ @ (\\d+),(\\d+): (\\d+)x(\\d+)')
    # Specify the maximum fabric dimensions
    N = 1000
    # Initialize an array for the fabric
    fabric = [0] * (N * N)
    # For each claim
    for line in f:
        # Regex it & Extract Values
        match = pattern.match(line)
        x = int(match.group(1))
        y = int(match.group(2))
        w = int(match.group(3))
        h = int(match.group(4))
        # Fill the fabric values
        for i in range(x, x + w):
            for j in range(y, y + h):
                fabric[i * N + j] += 1
    # Sum the squares with more than 1 claim
    overlapping = 0
    for j in range(N):
        for i in range(N):
            if fabric[i * N + j] > 1:
                overlapping += 1
    
    return overlapping

def main():
    return _part1()