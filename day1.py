import math
import re

filename = "input1.txt"
with open(filename) as file:
    input = [line.rstrip() for line in file]

# Part 1
total = 0
for line in input:
    nums = [char for char in line if char.isdigit()]
    assert len(nums) > 0, f"Bad input - no digits found in line {line}"
    total += int("".join(nums[0] + nums[-1]))
print(total)

# Part 2
DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

total = 0

for line in input:
    first_index, last_index = math.inf, -1
    first_digit, last_digit = -1, -1

    for digit in DIGITS:
        indices = [match.start() for match in re.finditer(digit, line)]
        if not indices:  # No appearances of digit in line
            continue
        if indices[0] < first_index:
            first_index = indices[0]
            first_digit = digit
        if indices[-1] > last_index:
            last_index = indices[-1]
            last_digit = digit

    total += int(DIGITS[first_digit] + DIGITS[last_digit])

print(total)
