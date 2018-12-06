""""Day 1: Chronal Calibration
https://adventofcode.com/2018/day/1
Part 1: What is the resulting frequency
Part 2: What is the first frequency your device reaches twice?
"""

from functools import reduce

def _load_file():
    # Open the file in read-only mode
    return open('data/day1.txt', 'r')

def _part1():
    """Part 1
    Reads from the input data and 'adds' it to the total.
    Python is smart and figures out +43 means 43 and -8 means -8
    Returns:
        Integer: Frequency tally from data
    """
    f = _load_file()
    # map(lambda l: int(l), f) converts each line to an int and returns as a list
    # reduce(lambda x, y: x + y, ~) sums the integers
    return reduce(lambda x, y: x + y, map(lambda l: int(l), f))

def _part2():
    """Part 2
    Saves current frequency and compares it against a set of previously encountered values
    Returns the first time frequency is found in frequencies
    Returns:
        Integer: First frequency found that was already encountered
    """
    f = _load_file()

    frequency = 0           # Current Frequency
    frequencies = set()     # Previous Frequencies

    # Transform the data to integers & save as a list 
    #   Saving as a the map would actually re-run the function in the loop
    deltas = list(map(lambda l: int(l), f))

    # Infinite loop
    while True:
        # For each value in the list of frequency deltas
        for delta in deltas:
            # A frequency delta of None or 0 would change nothing (I didn't look at the list for long)
            if delta:
                # Update the current frequency
                frequency += delta
                # Search the previously encountered frequencies
                #   If frequency previously encountered
                if frequency in frequencies:
                    return frequency
                # Else this is the first time the frequency was encountered
                #   and we add it to the list to be able to check if we encounter it again
                frequencies.add(frequency)

def main():
    return _part1(), _part2()
