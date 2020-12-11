from enum import Enum

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()


def validate(mode):
    components = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    validPassports = 0
    parts = ""

    for line in data:

        if line == data[-1]:
            # This is the last line, add it!
            parts = parts + line.strip("\n") + " "

        if line == "\n" or line == data[-1]:
            # Process it, it's done
            parts = parts[:-1].split(" ")
            passport = {}
            for part in parts:
                moreParts = part.split(":")
                passport[moreParts[0]] = moreParts[1]

            valid = 1
            for component in components:
                if not passport.get(component) and component != "cid":
                    valid = 0
                    break
                else:
                    if mode == 2:
                        # Do extended validation
                        val = passport.get(component)
                        if component == "byr":
                            if len(str(val)) != 4 or int(val) < 1920 or int(val) > 2002:
                                valid = 0
                                print("byr invalid")
                                break
                        elif component == "iyr":
                            if len(str(val)) != 4 or int(val) < 2010 or int(val) > 2020:
                                valid = 0
                                print("iyr invalid")
                                break
                        elif component == "eyr":
                            if len(str(val)) != 4 or int(val) < 2020 or int(val) > 2030:
                                valid = 0
                                print("eyr invalid")
                                break
                        elif component == "hgt":
                            if not (val[-2:] == "in" or val[-2:] == "cm"):
                                valid = 0
                                print("hgt invalid 1")
                                break
                            elif val[:-2].isnumeric():
                                if val[-2:] == "in":
                                    if int(val[:-2]) < 59 or int(val[:-2]) > 76:
                                        valid = 0
                                        print("hgt invalid 2")
                                        break
                                else:
                                    if int(val[:-2]) < 150 or int(val[:-2]) > 193:
                                        valid = 0
                                        print("hgt invalid 3")
                                        break
                            else:
                                valid = 0
                                break
                        elif component == "hcl":
                            if len(str(val)) != 7 or val[0:1] != "#":
                                valid = 0
                                break
                            else:
                                no = False
                                for letter in val[1:]:
                                    if not (letter.isnumeric() or letter == "a" or letter == "b" or
                                            letter == "c" or letter == "d" or letter == "e" or letter == "f"):
                                        no = True
                                if no:
                                    valid = 0
                                    break
                        elif component == "ecl":
                            if not (val == "amb" or val == "blu" or val == "brn" or val == "gry" or
                                    val == "grn" or val == "hzl" or val == "oth"):
                                valid = 0
                                break
                        elif component == "pid":
                            if len(str(val)) != 9 or not val.isnumeric():
                                valid = 0
                                break

            print(("Valid " if valid else "Invalid ") + str(passport))
            validPassports = validPassports + valid
            parts = ""
        else:
            # Append it, not done
            parts = parts + line.strip("\n") + " "

    return validPassports


print("Part 1: " + str(validate(1)))
print("Part 2: " + str(validate(2)))
