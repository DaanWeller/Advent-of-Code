def main():
    f = open("2023/day2/input_eva.txt")
    games_list = f.readlines()
    
    sum_games = 0

    game_id = 1

    for game in games_list:
        possible = True
        reveals = split_game_reveals(game)        

        for reveal in reveals:
            if test_reveal_legality(reveal) == False:
                possible = False
        
        if possible:
            sum_games += game_id
            
        game_id += 1

    print(sum_games)
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

if __name__ == "__main__":
    main()