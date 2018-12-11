""""Day 5: Alchemical Reduction
https://adventofcode.com/2018/day/5
Part 1: How many units remain after fully reacting the polymer you scanned?
Part 2: What is the length of the shortest polymer you can produce?
I'm sure there's a faster way to do this, but it works
"""

from pathlib import Path

def _load_file():
    # Open the file in read-only mode
    return open('data/day5.txt', 'r')

def _react(polymer):
    # Create a list of all possible reactions
    tests = [
        "Aa", "aA",
        "Bb", "bB",
        "Cc", "cC",
        "Dd", "dD",
        "Ee", "eE",
        "Ff", "fF",
        "Gg", "gG",
        "Hh", "hH",
        "Ii", "iI",
        "Jj", "jJ",
        "Kk", "kK",
        "Ll", "lL",
        "Mm", "mM",
        "Nn", "nN",
        "Oo", "oO",
        "Pp", "pP",
        "Qq", "qQ",
        "Rr", "rR",
        "Ss", "sS",
        "Tt", "tT",
        "Uu", "uU",
        "Vv", "vV",
        "Ww", "wW",
        "Xx", "xX",
        "Yy", "yY",
        "Zz", "zZ"
    ]
    reaction = True
    # While reactions are still happening
    while reaction == True:
        reaction = False
        # Test each reaction combination
        for test in tests:
            # If two units 'react' remove them from the polymer
            polymer_test = polymer.replace(test, '')
            reaction = reaction or (polymer != polymer_test)
            polymer = polymer_test
    return polymer

def _part1():
    """Part 1
    Initiates the polymer reaction
    Returns:
        Integer: Length of the polymer after reacting
    """
    f = _load_file()
    polymer = f.read().rstrip('\n')
    polymer = _react(polymer)
    return len(polymer)

def _part2():
    """Part 2
    Tests each polymer string with a specific unit removed
    Returns:
        Integer: Length of the shortest polymer
    """
    f = _load_file()
    polymer = f.read().rstrip('\n')
    shortest_polymer = polymer
    units = set(polymer)
    for unit in units:
        unit_value = ord(unit) - 65
        # Only check lowercase characters
        if unit_value < 26:
            # Remove the characters and react
            polymer_test = polymer.replace(unit, '')
            polymer_test = polymer_test.replace(chr(unit_value + 32 + 65), '')
            polymer_test = _react(polymer_test)
            if len(polymer_test) < len(shortest_polymer):
                shortest_polymer = polymer_test
    return len(shortest_polymer)

def main():
    return _part1(), _part2()
