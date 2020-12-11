print("Welcome to the super expense report fixer upper program .jpg 2000 inator!")

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()


def part1():
    for i in data:
        for j in data:
            if int(i) + int(j) == 2020:
                return int(i) * int(j)


def part2():
    for i in data:
        for j in data:
            for k in data:
                if int(i) + int(j) + int(k) == 2020:
                    return int(i) * int(j) * int(k)


print(part1())
print(part2())
