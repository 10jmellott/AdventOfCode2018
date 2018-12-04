""""Day 1: Chronal Calibration</a>
https://adventofcode.com/2018/day/1#part2
Part 2
What is the first frequency your device reaches twice?
"""

def main():
    """Entry Point
    Saves current frequency and compares it against a set of previously encountered values
    Returns the first time frequency is found in frequencies
    Returns:
        Integer: First frequency found that was already encountered
    """

    frequency = 0           # Current Frequency
    frequencies = set()     # Previous Frequencies

    # Open the file in read-only mode
    f = open('data/day1/part1.txt', 'r')
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
