import builtins


def main():
    f = open("../inputs/d10.txt")
    joltages = [int(line.rstrip('\n')) for line in f]
    f.close()

    print(f"Part 1: {part1(joltages)}")
    print(f"Part 2: {part2(joltages)}")

def part1(nums):
    built_in_adapter = max(nums) + 3
    current_charge = 0

    num_1j = 0
    num_3j = 0

    while current_charge != built_in_adapter:
        if current_charge + 1 in nums:
            current_charge += 1
            num_1j += 1
        elif current_charge + 2 in nums:
            current_charge += 2
        elif current_charge + 3 in nums or current_charge + 3 == built_in_adapter:
            current_charge += 3
            num_3j += 1

    return num_1j * num_3j

def part2(nums):
    paths = {max(nums): 1}
    def _helper(current_charge):
        num_paths = 0

        if current_charge not in paths.keys():
            if current_charge + 1 in nums:
                num_paths += _helper(current_charge + 1)
            if current_charge + 2 in nums:
                num_paths += _helper(current_charge + 2)
            if current_charge + 3 in nums:
                num_paths += _helper(current_charge + 3)

            paths[current_charge] = num_paths
            return num_paths
        else:
            return paths[current_charge]

    return _helper(0)

if __name__ == "__main__":
    main()