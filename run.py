"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from problems import day01, day02, day03, day04, day05

def test(f, message):
    timer = stopwatch.Timer()
    timer.start()
    ret = f()
    timer.stop()
    print(message)
    if ret:
        print('  Solution: {}'.format(ret))
    print('  Elapsed: {}'.format(timer.elapsed()))
    print()

print('Advent of Code - https://adventofcode.com/2018')
print('----------------------------------------------')
print()
# test(day01.main, "Day 01")
# test(day02.main, "Day 02")
# test(day03.main, "Day 03")
# test(day04.main, "Day 04")
test(day05.main, "Day 05")
