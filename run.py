"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from problems.day01 import part1
from problems.day01 import part2

print('Advent of Code - https://adventofcode.com/2018')

timer = stopwatch.Timer()
timer.start()

ret1 = part1.main()
ret2 = part2.main()

timer.stop()

if ret1:
    print('  Solution Part 1: {}'.format(ret1))

if ret2:
	print('  Solution Part 2: {}'.format(ret2))

print('  Elapsed: {}'.format(timer.elapsed()))
