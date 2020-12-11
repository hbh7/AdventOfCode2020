# Day 2

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()

validPasswords = 0

for i in data:
    line = i.split(" ")

    range = line[0].split("-")
    low = int(range[0])
    high = int(range[1])
    letter = line[1].split(":")[0]
    password = line[2]

    count = 0
    for j in password:
        if j == letter:
            count = count + 1

    if high >= count >= low:
        validPasswords = validPasswords + 1

print("Day 2 Part 1: " + str(validPasswords))

# Part 2
validPasswords = 0
for i in data:
    line = i.split(" ")

    positions = line[0].split("-")
    p1 = int(positions[0]) - 1
    p2 = int(positions[1]) - 1
    letter = line[1].split(":")[0]
    password = line[2]

    if (password[p1] == letter) != (password[p2] == letter):
        validPasswords = validPasswords + 1

print("Day 2 Part 2: " + str(validPasswords))
