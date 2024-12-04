# Description: Day 3 of Advent of Code 2024

import re

def main():
    with open('input.txt') as f:
        data = str(f.readlines())

    pattern = r"mul\(\d*,\d*\)"

    muls = re.findall(pattern, data)

    total = 0
    
    for mul in muls:
        digits = re.findall(r"\d+", mul)
        product = int(digits[0]) * int(digits[1])
        total += product

    print(total)

if __name__ == '__main__':
    main()