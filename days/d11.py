from copy import deepcopy

def main():
    f = open("../inputs/d11.txt")
    seat_grid = [list(line.rstrip('\n')) for line in f]
    f.close()

    print(f"Part 1: {part1(seat_grid)}")
    print(f"Part 2: {part2(seat_grid)}")

def apply_rules_pt1(original):
    changed = False
    new_seats = deepcopy(original)
    for i in range(len(new_seats)):
        for j in range(len(new_seats[i])):
            if new_seats[i][j] == 'L':
                if count_adj_occupied(i, j, original) == 0:
                    new_seats[i][j] = '#'
                    changed = True
            elif new_seats[i][j] == '#':
                if count_adj_occupied(i, j, original) >= 4:
                    new_seats[i][j] = 'L'
                    changed = True

    return new_seats, changed

def count_adj_occupied(i, j, seats):
    count = 0

    def _helper(i, pass_self=False):
        side_count = 0
        if j - 1 >= 0:
            if seats[i][j - 1] == '#':
                side_count += 1

        if seats[i][j] == '#' and not pass_self:
            side_count += 1

        if j + 1 < len(seats[i - 1]):
            if seats[i][j + 1] == '#':
                side_count += 1

        return side_count

    if i - 1 >= 0:
        count += _helper(i - 1)

    count += _helper(i, pass_self=True)

    if i + 1 < len(seats):
        count += _helper(i + 1)

    return count

def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1

    return count

def part1(seats):
    copied = deepcopy(seats)
    while True:
        copied, changed = apply_rules_pt1(copied)

        if not changed:
            break

    return count_occupied(copied)

def count_far_occupied(i, j, seats):
    # List of changes for (j, i) coords, starting left going clockwise
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    occupied = 0

    for j_change, i_change in directions:
        current_i = i + i_change
        current_j = j + j_change

        while current_i >= 0 and current_i < len(seats) and current_j >= 0 and current_j < len(seats[current_i]):
            if seats[current_i][current_j] == '#':
                occupied += 1
                break
            elif seats[current_i][current_j] == 'L':
                break
            else:
                current_i += i_change
                current_j += j_change

    return occupied

def apply_rules_pt2(original):
    changed = False
    new_seats = deepcopy(original)

    for i in range(len(new_seats)):
        for j in range(len(new_seats[i])):
            if new_seats[i][j] == '.':
                continue

            visible_occupied = count_far_occupied(i, j, original)
            if visible_occupied == 0 and new_seats[i][j] == 'L':
                new_seats[i][j] = '#'
                changed = True
            elif visible_occupied >= 5 and new_seats[i][j] == '#':
                new_seats[i][j] = 'L'
                changed = True

    return new_seats, changed

def part2(seats):
    copied = deepcopy(seats)
    while True:
        copied, changed = apply_rules_pt2(copied)

        if not changed:
            break

    return count_occupied(copied)

if __name__ == "__main__":
    main()
