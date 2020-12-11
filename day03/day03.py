dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()

# Convert to list, remove newline
for i in range(len(data)):
    data[i] = list(data[i])[0:-1]


def checker(right, down):
    trees = 0
    row = 0
    col = 0
    while row < len(data):
        if data[row][col] == "#":
            trees = trees + 1
        row = row + down
        col = col + right

        if col > len(data[0]) - 1:
            col = col - len(data[0])
    return trees


print("Part 1: " + str(checker(3, 1)))
print("Part 2: " + str(checker(1, 1) * checker(3, 1) * checker(5, 1) * checker(7, 1) * checker(1, 2)))
