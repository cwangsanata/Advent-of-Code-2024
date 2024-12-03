# Description: Day 1 of Advent of Code 2024

with open('input.txt') as f:
    data = f.readlines()

data = [x.strip('\n') for x in data]

col1, col2 = [], []

for line in data:
    col1.append(int(line[0:5]))
    col2.append(int(line[8:]))

col1.sort()
col2.sort()

total_distance = 0

for i in range(len(col1)):
    curr_distance= abs(col1[i] - col2[i])
    total_distance += curr_distance

print(total_distance)

