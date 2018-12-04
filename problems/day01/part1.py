""""Day 1: Chronal Calibration</a>
https://adventofcode.com/2018/day/1
Part 1
what is the resulting frequency
"""

from functools import reduce

def main():
    """Entry Point
    Reads from the input data and 'adds' it to the total.
    Python is smart and figures out +43 means 43 and -8 means -8
    Returns:
        Integer: Frequency tally from data
    """
    # Open the file in read-only mode
    f = open('data/day1/part1.txt', 'r')
    # map(lambda l: int(l), f) converts each line to an int and returns as a list
    # reduce(lambda x, y: x + y, ~) sums the integers
    return reduce(lambda x, y: x + y, map(lambda l: int(l), f))
