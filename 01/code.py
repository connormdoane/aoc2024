with open("input.txt") as f:
    firstcol = [int(line.rstrip().split()[0]) for line in f]
    f.seek(0)
    secondcol = [int(line.rstrip().split()[1]) for line in f]

def part1(firstcol, secondcol):
    distance = 0
    while len(firstcol) != 0:
        smallest = [min(firstcol), min(secondcol)]
        distance += abs(smallest[0] - smallest[1])
        firstcol.remove(smallest[0])
        secondcol.remove(smallest[1])
    return distance

def part2(firstcol, secondcol):
    similarity = 0
    for first in firstcol:
        times = 0
        for second in secondcol:
            if first == second:
                times += 1
        similarity += first * times
    return similarity

if __name__ == "__main__":
    print(part1(firstcol.copy(), secondcol.copy()))
    print(part2(firstcol.copy(), secondcol.copy()))