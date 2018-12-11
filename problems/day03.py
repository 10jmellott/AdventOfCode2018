""""Day 3: No Matter How You Slice It
https://adventofcode.com/2018/day/3
Part 1: How many square inches of fabric are within two or more claims?
Part 2: What is the ID of the only claim that doesn't overlap?
"""

import re

class Claim:
    pattern = re.compile('#\\d+ @ (\\d+),(\\d+): (\\d+)x(\\d+)')

    def __init__(self, input):
        match = Claim.pattern.match(input)
        self.line = input
        self.x = int(match.group(1))
        self.y = int(match.group(2))
        self.x2 = self.x + int(match.group(3))
        self.y2 = self.y + int(match.group(4))
    
    def overlaps(self, other):
        if self.x > other.x2 or self.y > other.y2:
            return False
        if self.x2 < other.x or self.y2 < other.y:
            return False
        return True

    def overlaps_area(self, other):
        return (min(self.x2, other.x2) - max(self.x, other.x)) * (min(self.y2, other.y2) - max(self.y, other.y))

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
    # map the claims to objects
    claims = map(lambda line: Claim(line), f)
    # Specify the maximum fabric dimensions
    N = 1000
    overlapping = 0
    # Initialize an array for the fabric
    fabric = [0] * (N * N)
    # For each claim
    for claim in claims:
        # Fill the fabric values
        for i in range(claim.x, claim.x2):
            for j in range(claim.y, claim.y2):
                fabric[i * N + j] += 1
                # The first time a fabric is counted twice, we add one to overlapping
                #  This avoids double-counting spaces that overlap 3+ times
                if fabric[i * N + j] == 2:
                    overlapping += 1
    return overlapping

def _part2():
    """Part 2
    Use regex to parse the input (claims).
    Map the claims to the Claim class for easier usage
    Check each claim against each other claim
    Returns:
        String: Corresponding line of the claim
    """
    # load the input
    f = _load_file()
    # map the claims to objects
    claims = list(map(lambda line: Claim(line), f))
    # create a list of unique claims
    unique = list()
    # go through each claim
    for claim in claims:
        # make a list of claims to remove if deemed no longer unique
        toremove = list()
        # test against all previously found unique claims
        for uniqueClaim in unique:
            # check if the claim overlaps with any unique
            if claim.overlaps(uniqueClaim):
                # if they do overlap, neither is unique
                toremove.append(uniqueClaim)
        # remove any claims found to not be unique
        for r in toremove:
            unique.remove(r)
        # if no claims were found that were unique (so far) then this one is
        if len(toremove) == 0:
            unique.append(claim)
    # I'm just gonna assume there is one here, YOLO
    return unique[0].line

def main():
    return _part1(), _part2()
