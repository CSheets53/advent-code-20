def main():
    f = open("../inputs/d7.txt")
    rule_strs = [line.rstrip('\n') for line in f]
    f.close()

    rules = generate_rules(rule_strs)

    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules)}")

def generate_rules(rule_strs: str):
    rules = {}

    for rule in rule_strs:
        bag_spl = rule.split(" bags contain ")
        parent = bag_spl[0]
        children_str = bag_spl[1]

        if "no" in children_str:
            rules[parent] = []
        elif ',' in children_str:
            spl = children_str.split(", ")
            children = []
            for contained in spl:
                contained_spl = contained.split()
                # Ex: [1, dark, olive, bag]
                count = int(contained_spl[0])
                bag_type = f"{contained_spl[1]} {contained_spl[2]}"
                children.append((count, bag_type))

            rules[parent] = children
        else:
            # Only 1 child
            spl = children_str.split() # Ex: [1, shiny, gold, bag.]
            count = int(spl[0])
            bag_type = f"{spl[1]} {spl[2]}"
            rules[parent] = [(count, bag_type)]

    return rules

def part1(rules: dict):
    child_bags = ["shiny gold"]
    unique_parents = set()

    while child_bags:
        current_child_to_find = child_bags.pop()

        for key, children in rules.items():
            for bag_info in children:
                if bag_info[1] == current_child_to_find:
                    child_bags.append(key)
                    unique_parents.add(key)
                    break

    return len(unique_parents)

def part2(rules: dict):
    def _count_contained_bags(current_bag):
        children = rules[current_bag]
        if not children:
            return 0

        total_count = 0
        for bag in children:
            total_count += (bag[0] + bag[0] * _count_contained_bags(bag[1]))

        return total_count

    return _count_contained_bags("shiny gold")

if __name__ == "__main__":
    main()
