def main():
    f = open("2024/day2/input_eva.txt")
    print("Using file " + f.name)
    reports = f.readlines()

    sum_pt1 = 0
    sum_pt2 = 0
    for report in reports:
        if is_report_safe(report):
            sum_pt1 += 1
        
        if is_report_safe_dampened(report):
            sum_pt2 += 1
    
    print(reports[-1])

    print("The answer to part 1 is " + str(sum_pt1))   

    print("The answer to part 2 is " + str(sum_pt2))   

    return 0


def is_report_safe_dampened(report: str):    
    lvls = report.split()

    lvls_reversed = lvls.copy()
    lvls_reversed.reverse()

    return sliding_window(lvls, True)


def sliding_window(lvls: list, joker: bool):
    increasing = (int(lvls[1]) > int(lvls[0]))

    for i in range(len(lvls) - 1):
        prev_lvl = int(lvls[i])

        lvl = int(lvls[i+1])

        if not is_lvl_safe(increasing, prev_lvl, lvl):
            if joker:
                lvls_0 = lvls.copy()
                lvls_0.pop(0)
                lvls_1 = lvls.copy()
                lvls_1.pop(i)
                lvls_2 = lvls.copy()
                lvls_2.pop(i+1)

                if sliding_window(lvls_1, False) or sliding_window(lvls_2, False) or sliding_window(lvls_0, False):
                    return True


                # return (sliding_window(lvls_1, False) or sliding_window(lvls_2, False))
            
            return False

    return True

 
def is_lvl_safe(increasing: bool, prev_lvl: int, lvl: int):

    safe = ( (lvl > prev_lvl) == increasing)
    
    if abs(lvl - prev_lvl) < 1 or abs(lvl - prev_lvl) > 3:
        safe = False

    return safe



def is_report_safe(report: str):
    safe = True
    
    lvls = report.split()

    prev_lvl = int(lvls[0])

    increasing = (int(lvls[1]) > int(lvls[0]))        
       
    for i in range(len(lvls) -1):

        lvl = int(lvls[i+1])

        if not is_lvl_safe(increasing, prev_lvl, lvl):
            safe = False
            return safe

        prev_lvl = lvl
    
    return safe




if __name__ == "__main__":
    main()