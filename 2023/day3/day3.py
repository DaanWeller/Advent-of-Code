import regex as re

def main():
    f = open('2023/day3/input_eva.txt')
    print("Using file " + f.name)
    lines = f.readlines()
    
    # To keep track of the matches in symbols and numbers
    pl_syms = []
    cl_syms = []
    nl_syms = []

    pl_nrs = []
    cl_nrs = []
    nl_nrs = []

    part_nrs = []

    # We will always be looking at the "next line"
    for line in lines:
        pl_syms = cl_syms
        cl_syms = nl_syms
        nl_syms = get_matches("[^0-9|.|\n]", line)


        pl_nrs = cl_nrs
        cl_nrs = nl_nrs
        nl_nrs = get_matches("[0-9]+", line)

        part_nrs.extend(get_part_nrs(cl_nrs, pl_syms, cl_syms, nl_syms))

    # Now run the previous step once more, as we would otherwise miss the last line. 
    # Clearing the next line as those are no longer useful
    pl_syms = cl_syms
    cl_syms = nl_syms
    nl_syms = []


    pl_nrs = cl_nrs
    cl_nrs = nl_nrs
    nl_nrs = []

    part_nrs.extend(get_part_nrs(cl_nrs, pl_syms, cl_syms, nl_syms))

    print(sum(part_nrs))


    return 0


# Calculate the part numbers based on the lines found
def get_part_nrs(numbers: list, prev_syms: list, cur_syms: list, next_syms: list):
    parts = []
    
    # Find the actual coordinates for the symbols in the previous/current/next line
    prev_sym_coords = []
    for sym in prev_syms:
        prev_sym_coords.append(sym.span()[0])
    
    cur_sym_coords = []
    for sym in cur_syms:
        cur_sym_coords.append(sym.span()[0])

    next_sym_coords = []
    for sym in next_syms:
        next_sym_coords.append(sym.span()[0])
    

    # For each number, compare it against the coordinates of the symbols in the adjacent lines
    for number in numbers:
        nr_coords = number.span()

        coord_range = [*range(nr_coords[0], nr_coords[1], 1)]
        
        
        for coord in coord_range:
            if ( (coord-1) in cur_sym_coords ):
                parts.append(int(number.group()))
                break
            elif ( (coord+1) in cur_sym_coords ):
                parts.append(int(number.group()))
                break
            elif( coord in prev_sym_coords or coord in next_sym_coords):
                parts.append(int(number.group()))
                break
            elif( (coord-1) in prev_sym_coords or (coord-1) in next_sym_coords):
                parts.append(int(number.group()))
                break
            elif( (coord+1) in prev_sym_coords or (coord+1) in next_sym_coords):
                parts.append(int(number.group()))
                break

    return parts
   

# Get the matches for a regex in a string
def get_matches (regx: str, line: str):
    index = 0
    matches = []
    dots = "..."
    while len(line) > index:
        match = re.search(regx, line)
        if (match != None):
            matches.append(match)
            replacement = dots[0:(match.span()[1] - match.span()[0])]
            line = re.sub(regx, replacement, line, 1)
        else:
            index = len(line)
    
    return matches
    

if __name__ == "__main__":
    main()