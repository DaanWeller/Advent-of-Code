import regex as re

def main():
    f = open("2024/day3/input_eva.txt")
    print("Using file " + f.name)
    
    lines = f.readlines()

    part_1_solver(lines)
    part_2_solver(lines)

    return 0


# Finds and prints the solution to part 1
def part_1_solver(lines: list):
    pt1_answer = calc_muls(lines)
    
    print("The answer to part 1 is " + str(pt1_answer))
    return


# Finds and prints the solution to part 2
def part_2_solver(lines: list):
    pt2_answer = 0

    # As the instructions don't refer to the input as separate lines, concatenate the input to a single string
    concatenated_line = ""
    for line in lines:
        concatenated_line += line
    
    enabled_strings = find_enabled_instructions(concatenated_line)
    pt2_answer = calc_muls(enabled_strings)

    print("The answer to part 2 is " + str(pt2_answer))
    return


# Takes a string and returns the parts of that string where the multiplications are enabled
# A part of the string is disabled if it was preceded by "don't()" and no "do()" has since come up
def find_enabled_instructions(line: str):
    enabled_instructions = []
    
    split_instructions = re.split("don't\(\)", line)

    # If the original line did not start with "don't()", append the first split result as it is considered enabled
    if re.match("don't\(\)%", line) == None:
        enabled_instructions.append(split_instructions[0])
        split_instructions.pop(0)
    
    # For all other instructions, split on the first "do()" and append whatever follows
    for instruction in split_instructions:
        split_ins = re.split("do\(\)", instruction, 1)
        # Only append if there was at least one instance of "do()" found
        if len(split_ins) == 2:        
            enabled_instructions.append(split_ins[1])


    return enabled_instructions

# Takes a list of strings, calculates the sum of the valid multiplications in the strings and returns that sum
# A valid multiplication looks like mul(X,Y), with X and Y being any integer
def calc_muls(lines: list):
    matches = []

    for line in lines:
        matches.extend(re.findall('mul\([0-9]+,[0-9]+\)', line))
    
    sum = 0
    for match in matches:
        sum += multiply_mul(match)  
    
    return sum



# Takes a string formatted as "mul(X,Y)" and calculates the result of X*Y
def multiply_mul(mul: str):
    
    values = re.findall('[0-9]+', mul)
    
    result = 0

    if len(values) == 2:
        result = int(values[0]) * int(values[1])
    else:
        raise Exception("The string passed to multiply_mul was incorrect. String given: " + mul)
    
    return result


if __name__ == "__main__":
    main()