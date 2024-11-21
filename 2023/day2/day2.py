def main():
    f = open("2023/day2/input_eva.txt")
    print("Using file " + f.name)
    games_list = f.readlines()
    
    sum_games = 0
    sum_cubes_cubed = 0

    game_id = 1

    for game in games_list:
        min_cubes = [0, 0, 0]
        possible = True
        reveals = split_game_reveals(game)        

        for reveal in reveals:
            # Check legality for part 1
            if test_reveal_legality(reveal) == False:
                possible = False
            
            # Calculated the cubes revealed for part 2
            revealed_cubes = calc_min_cubes(reveal)            

            if revealed_cubes[0] > min_cubes[0]:
                min_cubes[0] = revealed_cubes[0]
            
            if revealed_cubes[1] > min_cubes[1]:
                min_cubes[1] = revealed_cubes[1]

            if revealed_cubes[2] > min_cubes[2]:
                min_cubes[2] = revealed_cubes[2]

        # If the game was legal, add the ID to the sum
        if possible:
            sum_games += game_id
        
        # Calculate the cube of the revealed cubes
        cubes_cubed = min_cubes[0] * min_cubes[1] * min_cubes[2]
        sum_cubes_cubed += cubes_cubed

        game_id += 1

    print("The answer to part 1 is " + str(sum_games))

    print("The answer to part 2 is " + str(sum_cubes_cubed))

    return 0

# Take a single game and return the sets of revealed cubes in a list
def split_game_reveals(game_line: str):
    reveals_string = game_line.split(sep=':')[1]
    reveals_list = reveals_string.split(sep=';')
    return reveals_list

# Test the legality of a single set of revealed cubes
def test_reveal_legality(revealed_set):
    legal = True

    red_base = 12
    green_base = 13
    blue_base = 14
    
    nr_red = 0
    nr_green = 0
    nr_blue = 0

    # Check each and count the amount of cubes revealed
    cubes = revealed_set.split(sep=',')
    for cube in cubes:
        if 'red' in cube:
            nr_red += int(cube.split()[0])
        elif 'green' in cube:
            nr_green += int(cube.split()[0])
        elif 'blue' in cube:
            nr_blue += int(cube.split()[0])

    if nr_red > red_base or nr_green > green_base or nr_blue > blue_base:
        legal = False
    
    return legal

# Calculate the minimum number of cubes required for the revealed set
def calc_min_cubes(revealed_set):
    nr_red = 0
    nr_green = 0
    nr_blue = 0

    # Check each and count the amount of cubes revealed
    cubes = revealed_set.split(sep=',')
    for cube in cubes:
        if 'red' in cube:
            nr_red += int(cube.split()[0])
        elif 'green' in cube:
            nr_green += int(cube.split()[0])
        elif 'blue' in cube:
            nr_blue += int(cube.split()[0])
    
    min_cubes = (nr_red, nr_green, nr_blue)

    return min_cubes



if __name__ == "__main__":
    main()