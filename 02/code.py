with open("input.txt") as f:
    lines = [line.rstrip().split() for line in f]
    lines = [[int(n) for n in line] for line in lines]

def part1(lines):
    count = 0
    for line in lines:
        inc = True
        dec = True
        smalldiff = True
        for i in range(len(line)-1):
            # Check for not increasing nor decreasing
            if line[i] <= line[i+1]:
                dec = False
            if line[i] >= line[i+1]:
                inc = False
            # Check for small differences
            if abs(line[i] - line[i+1]) > 3:
                smalldiff = False
        if (inc or dec) and smalldiff:
            count += 1
    return count

def testline(line):
    inc = True
    dec = True
    smalldiff = True
    for i in range(len(line)-1):
        # Check for not increasing nor decreasing
        if line[i] <= line[i+1]:
            dec = False
        if line[i] >= line[i+1]:
            inc = False
        # Check for small differences
        if abs(line[i] - line[i+1]) > 3:
            smalldiff = False
    if (inc or dec) and smalldiff:
        return True
    return False


def part2(lines):
    count = 0
    for line in lines:
        # Test whether it works without a removal
        singleTruth = testline(line)
        if not singleTruth:
            # Attempt all possible removals
            for removal in range(len(line)):
                editedline = line.copy()
                editedline.pop(removal)
                if testline(editedline):
                    singleTruth = True
        if singleTruth:
            count += 1
    return count


if __name__ == "__main__":
    print(part1(lines))
    print(part2(lines))