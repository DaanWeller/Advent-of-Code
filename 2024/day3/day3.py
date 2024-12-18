import regex as re

def main():
    f = open("2024/day3/input_eva.txt")
    print("Using file " + f.name)
    
    lines = f.readlines()

    pt1_answer = calc_muls(lines)
    
    print("The answer to part 1 is " + str(pt1_answer))

    return 0

# Takes a list of strings, calculates the sum of the valid multiplications in the strings and returns that sum
# A valid multiplication looks like mul(X,Y), with X and Y being any integer
def calc_muls(lines: list):
    # The pattern to match against
    pattern = 'mul\([0-9]+,[0-9]+\)'
    matches = []

    for line in lines:
        matches.extend(re.findall(pattern, line))
    
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