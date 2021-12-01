class Password:
    """Basic password class to store info from each line"""
    def __init__(self, data: str):
        # Format of data: min-max letter: password
        # Ex: 1-3 a: abcde
        self.min = int(data[:data.index('-')]) # also pos 1
        self.max = int(data[(data.index('-') + 1):data.index(' ')]) # also pos 2
        self.letter = data[(data.index(' ') + 1):data.index(':')]
        self.password = data[(data.index(':') + 2):] # +2 to remove extra whitespace

def main():
    f = open('../inputs/d2.txt')
    lines = [line for line in f.readlines()]
    f.close()

    passwords = parse_input(lines)

    print(f"Part 1: {part1(passwords)}")
    print(f"Part 2: {part2(passwords)}")

def parse_input(lines):
    data = []

    for line in lines:
        password = Password(line)
        data.append(password)

    return data

def part1(passwords):
    """Passwords are valid if the given letter appears between min and max (inclusive) times in the password"""
    valid_count = 0

    for p in passwords:
        if p.letter in p.password:
            letter_count = p.password.count(p.letter)

            if letter_count >= p.min and letter_count <= p.max:
                valid_count += 1

    return valid_count

def part2(passwords):
    """With min representing position 1 and max representing position 2, passwords are valid if only one pos in the password contains the letter"""
    valid_count = 0

    for p in passwords:
        if (p.password[p.min - 1] == p.letter and p.password[p.max - 1] != p.letter) or \
            (p.password[p.min - 1] != p.letter and p.password[p.max - 1] == p.letter):
            valid_count += 1

    return valid_count

if __name__ == "__main__":
    main()
