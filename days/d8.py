def main():
    f = open("../inputs/d8.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    instructions = []
    for line in lines:
        instr_spl = line.split(' ')
        
        int_val = None
        if '+' in instr_spl[1]:
            int_val = int(instr_spl[1][1:])
        else:
            int_val = int(instr_spl[1])

        instructions.append((instr_spl[0], int_val))

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

def part1(instrs):
    accumulator = 0
    current_instruction_index = 0
    unique_instructions = []

    while True:
        if current_instruction_index in unique_instructions:
            return accumulator

        unique_instructions.append(current_instruction_index)
        instruction = instrs[current_instruction_index]
        if instruction[0] == "acc":
            accumulator += instruction[1]
            current_instruction_index += 1
        elif instruction[0] == "jmp":
            current_instruction_index += instruction[1]
        else:
            # nop
            current_instruction_index += 1

def run_instructions(instrs):
    accumulator = 0
    current_instruction_index = 0
    unique_instructions = []

    while True:
        if current_instruction_index in unique_instructions:
            return accumulator, False

        unique_instructions.append(current_instruction_index)
        instruction = instrs[current_instruction_index]
        if instruction[0] == "acc":
            accumulator += instruction[1]
            current_instruction_index += 1
        elif instruction[0] == "jmp":
            current_instruction_index += instruction[1]
        else:
            # nop
            current_instruction_index += 1

        if current_instruction_index == len(instrs):
            return accumulator, True

def part2(instrs):
    accumulator = 0

    original_instrs = instrs.copy()

    for i in range(len(instrs)):
        if "nop" == instrs[i][0]:
            instrs[i] = ("jmp", instrs[i][1])
        elif "jmp" == instrs[i][0]:
            instrs[i] = ("nop", instrs[i][1])

        accumulator, worked = run_instructions(instrs)
        if worked:
            return accumulator
        
        instrs = original_instrs.copy()

    return -1

if __name__ == "__main__":
    main()
