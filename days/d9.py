def main():
    f = open("../inputs/d9.txt")
    nums = [int(line.rstrip('\n')) for line in f]
    f.close()

    invalid_num = part1(nums)
    print(f"Part 1: {invalid_num}")
    print(f"Part 2: {part2(nums, invalid_num)}")

PREAMBLE_LEN = 25

def check_sum(target, sub_list):
    for i in range(len(sub_list) - 1):
        for j in range(len(sub_list)):
            if (sub_list[i] + sub_list[j]) == target:
                return True

    return False

def part1(nums):
    for i in range(PREAMBLE_LEN, len(nums)):
        # Check that 2 of the previous P_LEN nums could sum to current num
        current_num = nums[i]
        previous = nums[i-PREAMBLE_LEN:i]

        if not check_sum(current_num, previous):
            return current_num

    return -1

def check_contig_sum(target, sub_list):
    for i in range(len(sub_list) - 1):
        sum = sub_list[i]
        for j in range(i + 1, len(sub_list)):
            sum += sub_list[j]
            if sum == target:
                return sub_list[i:j+1]

    return None

def part2(nums, invalid):
    for i in range(PREAMBLE_LEN, len(nums)):
        previous = nums[i-PREAMBLE_LEN:i]

        winning_range = check_contig_sum(invalid, previous)
        if winning_range:
            return max(winning_range) + min(winning_range)

    return -1

if __name__ == "__main__":
    main()
