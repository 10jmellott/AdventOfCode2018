""""Day 4: Repose Record
https://adventofcode.com/2018/day/4
Part 1: What is the ID of the guard you chose multiplied by the minute you chose?
    * Guard who spent the most time asleep * the minute they slept the most
Part 2: What is the ID of the guard you chose multiplied by the minute you chose?
    * Find the highest recurring minute for any guard and multiply it by the guard's ID
    * This one was hard to phrase...
* Assumed only one guard can be on duty at a time
"""

from datetime import datetime
import re
from enum import Enum

class RecordType(Enum):
    SHIFT_CHANGE = 1,
    WAKE_UP = 2,
    FALL_ASLEEP = 3

class Record:
    pattern = re.compile('\\[(\\d+)-(\\d+)-(\\d+) (\\d+):(\\d+)\\] (.+)')
    wakeup = "wakes up"
    fallasleep = "falls asleep"
    gaurdpattern = re.compile('Guard #(\\d+) begins shift')

    def __init__(self, input):
        match = Record.pattern.match(input)
        timestamp = match.group(1) + '-' + match.group(2) + '-' + match.group(3) + ' ' + match.group(4) + ':' + match.group(5)
        # Saving the python time object so I don't have to do any time math myself...
        self.time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
        message = match.group(6)
        # Parse the message to determine the type of the message
        if message == Record.wakeup:
            self.Type = RecordType.WAKE_UP
        elif message == Record.fallasleep:
            self.Type = RecordType.FALL_ASLEEP
        else:
            self.Type = RecordType.SHIFT_CHANGE
            # Perform a second regex to get the guard ID
            match = Record.gaurdpattern.match(message)
            self.id = int(match.group(1))

def _load_file():
    # Open the file in read-only mode
    return open('data/day4.txt', 'r')

def _sortBy(item):
    # The time is suitable sorting
    return item.time

def _load_guard_info():
    # Load the input
    f = _load_file()
    # map the records to objects
    records = list(map(lambda line: Record(line), f))
    # The records aren't sorted by default
    records.sort(key=_sortBy, reverse=False)
    # The current guard id, assumes the first record is a shift change
    guardId = 0
    # Sets some default dictionaries
    guardSleepTime = {}
    guardSleepMinutes = {}
    # Loop through each record
    for record in records:
        # If the shift changed then change the guard id
        if record.Type is RecordType.SHIFT_CHANGE:
            guardId = record.id
        # If the guard fell asleep, then record the time they did
        elif record.Type is RecordType.FALL_ASLEEP:
            sleepStart = record.time
        # Else the guard has woken up and we need to record some metrics
        else:
            # Time math from when they fell asleep
            delta = int((record.time - sleepStart).total_seconds())
            
            # Add to the total time the guard sleeps
            if guardId in guardSleepTime:
                guardSleepTime[guardId] += delta
            else:
                guardSleepTime[guardId] = delta
            
            # Add to the minutes the guard slept
            minuteDict = {}
            if guardId in guardSleepMinutes:
                minuteDict = guardSleepMinutes[guardId]            
            deltaM = int(delta / 60)
            for t in range(deltaM):
                minute = ((sleepStart.minute + t) % 60)
                if minute in minuteDict:
                    minuteDict[minute] += 1
                else:
                    minuteDict[minute] = 1
            # (re)Set the minute definition for the guard
            guardSleepMinutes[guardId] = minuteDict
    # Return the parsed information
    return guardSleepTime, guardSleepMinutes

def _part1():
    """Part 1
    Pull the guard information.
    Find the guard with the most sleep time.
    Find the minute that guard was asleep the most.
    Returns:
        Integer: Guard Id * Minute
    """
    # Load shared guard info from part 1
    guardSleepTime, guardSleepMinutes = _load_guard_info()
    # Find the guard who spends the most time asleep
    sleepyGuardId = 0
    sleepyGuardTime = 0
    for guard in guardSleepTime:
        if guardSleepTime[guard] > sleepyGuardTime:
            sleepyGuardId = guard
            sleepyGuardTime = guardSleepTime[guard]
    # Find the minute that guard is asleep the most
    sleepyGuardMinute = 0
    sleepyGuardMinuteCount = 0
    for minute in guardSleepMinutes[sleepyGuardId]:
        if guardSleepMinutes[sleepyGuardId][minute] > sleepyGuardMinuteCount:
            sleepyGuardMinute = minute
            sleepyGuardMinuteCount = guardSleepMinutes[sleepyGuardId][minute]
    return sleepyGuardId * sleepyGuardMinute

def _part2():
    """Part 2
    Look through each guard and each minute that guard was 
    asleep and find the maximum recurring minute among all guards.
    Returns:
        Integer: Guard Id * Minute
    """
    # Load the shared parsing from Part 1
    _, guardSleepMinutes = _load_guard_info()
    # Find the maximum repeated minute and save the guard Id from that
    sleepyGuardId = 0
    sleepyGuardMinute = 0
    sleepyGuardMinuteCount = 0
    for guard in guardSleepMinutes:
        for minute in guardSleepMinutes[guard]:
            if guardSleepMinutes[guard][minute] > sleepyGuardMinuteCount:
                sleepyGuardId = guard
                sleepyGuardMinute = minute
                sleepyGuardMinuteCount = guardSleepMinutes[guard][minute]
    return sleepyGuardId * sleepyGuardMinute

def main():
    return _part1(), _part2()
