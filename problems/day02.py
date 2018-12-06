""""Day 2: Inventory Management System
https://adventofcode.com/2018/day/2
Part 1: What is the checksum?
Part 2: What letters are common between the two correct box IDs?
"""

def _load_file():
    # Open the file in read-only mode
    return open('data/day2.txt', 'r')

def _part1():
    """Part 1
    Pulls in the input and performs a simple character tally sum by
    going through each character and then compares it against each character again.
    Unoptimized!
    Checksum is defined as the inputs with one or more instance of a character
    repeating twice multiplied by the number of inputs with one or more instances
    of a character repeating exactly three times.
    Returns:
        Integer: Checksum value of the input
    """
    f = _load_file()
    # Loop through each word and tally the number with double and triple
    doubleCount = 0
    tripleCount = 0
    for line in f:
        # Null-check
        if line:
            # Assume neither double nor triple to start
            hasDouble = False
            hasTriple = False
            # Loop through each character twice and tally
            for char1 in line:
                count = 0
                for char2 in line:
                    if char1 == char2:
                        count += 1
                # If the character has double or triple then mark it
                hasDouble = hasDouble or count == 2
                hasTriple = hasTriple or count == 3
            # Each word can only trigger double / triple once
            # Making use of False = 0 and True = 1 here
            doubleCount += hasDouble
            tripleCount += hasTriple
    # Checksum is # doubles * # triples
    return doubleCount * tripleCount

def _part2():
    """Part 2
    Goes through each possible pair of input and compares each character.
    Short-circuit if a pair of inputs are found that differ by only one character.
    The comparison of a pair is also short circuited the moment a second difference is found.
    Returns:
        Integer: Common characters of nearly-identical ids
    """
    f = _load_file()
    # Convert to a list for loops
    lines = list(f)
    i = 0
    # For each test input
    for line1 in lines:
        i += 1
        n1 = len(line1)
        # For each other value (pair not tested)
        for line2 in lines[i:]:
            n2 = len(line2)
            # Ensure they are the same length, sanity check mostly
            if n1 == n2:
                # Save the bad character index
                badChari = -1
                # Test the characters
                for j in range(n1):
                    if line1[j] != line2[j]:
                        # If badCharacter not found yet
                        if badChari == -1:
                            badChari = j
                        # If we've previously encountered a bad character
                        else:
                            # Reset the bad character to indicate we broke early
                            badChari = -1
                            # Break early
                            break
                # If there was only one bad character, the value != -1 and we can return the common chars
                if badChari != -1:
                    return line1[:badChari] + line1[badChari + 1:]

def main():
    return _part1(), _part2()