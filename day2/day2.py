# Description: Day 2 of Advent of Code 2024

def main():
    with open('input.txt') as f:
        data = f.readlines()

    data = [x.strip('\n').split(' ') for x in data]
    data = [[int(char) for char in row] for row in data]

    count = 0

    # for row in data:

    #     increasing, decreasing = False, False
    #     if row[0] < row[1]:
    #         increasing = True
    #     elif row[0] > row[1]:
    #         decreasing = True

    #     for i in range(len(row) - 1):
    #         delta = abs(row[i + 1] - row[i])
    #         if ((row[i] < row[i + 1] and decreasing) or (row[i] > row[i + 1] and increasing)) and (delta < 1 or delta > 3): 
    #             continue
    #         else:
    #             count += 1
    #             increasing = False
    #             decreasing = False
    #             break
    
    for row in data:
        if increasingAndSafe(row) or decreasingAndSafe(row):
            count += 1
    print(count)

def increasingAndSafe(row):
    for i in range(len(row) - 1):
        if row[i] < row[i + 1] and safeDiff(row[i], row[i + 1]):
            continue
        else:
            return False
    return True

def decreasingAndSafe(row):
    for i in range(len(row) - 1):
        if row[i] > row[i + 1] and safeDiff(row[i], row[i + 1]):
            continue
        else:
            return False
    return True

def safeDiff(a, b):
    diff = abs(a - b)
    if 1 <= diff <= 3:
        return True
    return False
    
if __name__ == '__main__':
    main()