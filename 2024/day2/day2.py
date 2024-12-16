def main():
    f = open("2024/day2/input_eva.txt")
    print("Using file " + f.name)
    reports = f.readlines()

    sum = 0
    for report in reports:
        if is_safe(report):
            sum += 1
    
    print("The answer to part 1 is " + str(sum))   

    return 0


def is_safe(report: str):
    safe = True
    
    lvls = report.split()

    prev_lvl = int(lvls[0])

    if(int(lvls[1]) > prev_lvl):
        increasing = True
    else:
        increasing = False
        
       
    for i in range(len(lvls) -1):

        lvl = int(lvls[i+1])

        if lvl > prev_lvl and not increasing:
            safe = False
            break
        elif lvl < prev_lvl and increasing:
            safe = False
            break

        if abs(lvl - prev_lvl) < 1 or abs(lvl - prev_lvl) > 3:
            safe = False
            break

        prev_lvl = lvl
    
    return safe


if __name__ == "__main__":
    main()