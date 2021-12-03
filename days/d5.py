from numpy import arange
from numpy.core.fromnumeric import sort

ALL_SEAT_IDS = []
COLS = arange(8)
ROWS = arange(128)

def main():
    f = open("../inputs/d5.txt")
    passports = [line.rstrip('\n') for line in f]
    f.close()

    print(f"Part 1: {part1(passports)}")
    print(f"Part 2: {part2()}")

def find_row(row_instr):
    current_rows = ROWS
    for instr in row_instr:
        if instr == 'F':
            current_rows = current_rows[:(len(current_rows) // 2)]
        else:
            current_rows = current_rows[(len(current_rows) // 2):]

    return current_rows[0]

def find_col(col_instr):
    current_cols = COLS
    for instr in col_instr:
        if instr == 'L':
            current_cols = current_cols[:(len(current_cols) // 2)]
        else:
            current_cols = current_cols[(len(current_cols) // 2):]

    return current_cols[0]

def part1(passports):
    """Finds the highest seat ID on a boarding pass (row * 8 + col)"""
    max_seat_id = -1
    for p in passports:
        row = find_row(p[:7])
        col = find_col(p[7:])
        seat_id = row * 8 + col

        ALL_SEAT_IDS.append(seat_id)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id

def part2():
    """Finds my seat ID, which is the only one missing from a sorted list"""
    sorted_ids = sorted(ALL_SEAT_IDS)

    for i in range(len(sorted_ids) - 1):
        if (sorted_ids[i] + 1) != sorted_ids[i + 1]:
            return sorted_ids[i] + 1

    return -1

if __name__ == "__main__":
    main()
