def main():
    f = open('../inputs/d1.txt')
    lines = [int(line) for line in f.readlines()]
    f.close()

    lines = set(lines) # makes *in* lookup O(1)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def part1(lines):
    """Find the two entries that sum to 2020, and return their product"""
    for x in lines:
        y = 2020 - x
        if y in lines:
            return x * y

def part2(lines):
    """Find the three entries that sum to 2020, and return their product"""
    for x in lines:
        for y in lines:
            z = 2020 - (x + y)
            if z in lines:
                return x * y * z

if __name__ == "__main__":
    main()
