REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} # omit cid

def main():
    f = open("../inputs/d4.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    passports = parse_passports(lines)

    print(f"Part 1: {part1(passports)}")
    print(f"Part 2: {part2(passports)}")

def parse_passports(input):
    passports = []

    index = 0
    for line in input:
        if len(line):
            if index >= len(passports):
                passports.append(line)
            else:
                passports[index] += f" {line}"
        else:
            index += 1

    return passports

def all_fields_present(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return False

    return True

def part1(passports):
    """Checks each passport for validity, where valid has all the req. fields"""
    valid_count = 0
    for p in passports:
        if all_fields_present(p):
            valid_count += 1

    return valid_count

def validate_fields(passport):
    valid_ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    fields = passport.split(' ')

    for f in fields:
        name = f[:f.index(':')]
        val = f[(f.index(':') + 1):]

        if name == "byr":
            if len(val) != 4 or not val.isnumeric() or int(val) < 1920 or int(val) > 2002:
                return False
        elif name == "iyr":
            if len(val) != 4 or not val.isnumeric() or int(val) < 2010 or int(val) > 2020:
                return False
        elif name == "eyr":
            if len(val) != 4 or not val.isnumeric() or int(val) < 2020 or int(val) > 2030:
                return False
        elif name == "hgt":
            if "cm" in val:
                cm_val = int(val[:val.index("cm")])
                if cm_val < 150 or cm_val > 193:
                    return False
            elif "in" in val:
                in_val = int(val[:val.index("in")])
                if in_val < 59 or in_val > 76:
                    return False
            else:
                return False
        elif name == "hcl":
            if '#' not in val or not val[1:].isalnum():
                return False
        elif name == "ecl":
            if val not in valid_ecls:
                return False
        elif name == "pid":
            if len(val) != 9 or not val.isnumeric():
                return False
        else:
            pass # name == cid

    return True

def part2(passports):
    """Checks each passport for validity where all req. fields are present and follow given rules"""
    valid_count = 0

    for p in passports:
        if not all_fields_present(p):
            continue

        valid_count += 1 if validate_fields(p) else 0

    return valid_count

if __name__ == "__main__":
    main()
