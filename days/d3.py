def main():
    f = open('../inputs/d3.txt')
    map_chunk = [line.rstrip('\n') for line in f]
    f.close()

    part1_ans = part1(map_chunk)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2(map_chunk, part1_ans)}")

def part1(map_chunk, down=1, right=3):
    """Count how many trees are encountered traveling the map going right 3 and down 1"""
    LINE_LENGTH = len(map_chunk[0])
    TREE = '#'

    tree_count = 0
    square_index = 0    # index of the line

    # While we haven't reached the bottom of the slope
    for line_index in range(0, len(map_chunk), down):
        # Check if we need to wrap around
        if square_index >= LINE_LENGTH:
            square_index -= LINE_LENGTH

        if map_chunk[line_index][square_index] == TREE:
            tree_count += 1

        square_index += right

    return tree_count

def part2(map_chunk, part1_ans):
    """Calculate the product of the number of trees hit for a list of varying slopes"""
    # (down, right) -- omitted slope calculated in part1
    slopes = [(1, 1), (1, 5), (1, 7), (2, 1)]
    
    total_tree_product = part1_ans
    for slope in slopes:
        total_tree_product *= part1(map_chunk, slope[0], slope[1])

    return total_tree_product

if __name__ == "__main__":
    main()

