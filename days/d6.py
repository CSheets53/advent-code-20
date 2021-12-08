def main():
    f = open("../inputs/d6.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    groups = []
    new_group = []
    for line in lines:
        if line:
            new_group.append(line)
        else:
            groups.append(new_group)
            new_group = []

    groups.append(new_group)

    print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")

def part1(groups):
    """Calculate the sum of each group's number of questions answered 'yes'"""
    count = 0
    for group in groups:
        all_answers_str = ''.join(group)
        chars = set(all_answers_str)
        count += len(chars)

    return count

def part2(groups):
    """Calculate the sum of the number of questions *everyone* answered 'yes'"""
    count = 0
    for group in groups:
        best_str = group[0]

        for i in range(1, len(group)):
            remove_letters = []
            for c in best_str:
                if c not in group[i]:
                    remove_letters.append(c)

            for c in remove_letters:
                best_str = best_str.replace(c, '')

        count += len(best_str)

    return count

if __name__ == "__main__":
    main()
