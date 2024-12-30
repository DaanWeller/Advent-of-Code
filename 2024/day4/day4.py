def main():
    f = open("2024/day4/input_eva.txt")
    print("Using file " + f.name)
    lines = f.readlines()

    # Assuming consistent line length and ignoring the newline character
    line_length = len(lines[0])-1

    print("The answer to part 1 is " + str(count_xmas(lines, line_length)))

    return 0

# count the occurrences of XMAS in the given input
def count_xmas(lines: list, line_length: int):
    count = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'X':
                count += test_directions(lines, line_length, x, y)
    
    return count

# Check each direction to see if XMAS can be found in that direction 
def test_directions(lines: list, line_length: int, x: int, y: int):
    count = 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1), 
    (0, -1), (0, 1), 
    (1, -1,), (1, 0), (1, 1)]
    
    for d in directions:
        if test_position(lines, line_length, d, x, y):
            if test_xmas(lines, line_length, d, x, y):
                count+= 1

    return count

# Check if there is enough space in the given direction to form the word XMAS 
def test_position(lines: list, line_length: int, direction: tuple, x: int, y: int):
    if 0 <= y + direction[1] * 3 < len(lines) and 0 <= x + direction[0] * 3 < line_length:
        return True
    else:
        return False

# Check if XMAS is found in the given direction
def test_xmas(lines: list, line_length: int, direction: tuple, x: int, y: int):
    found = True
    target = 'XMAS'

    for i, c in enumerate(target):
        if lines[y + direction[1] * i][x + direction[0] * i] != c:
            found = False
    
    return found


if __name__ == "__main__":
    main()