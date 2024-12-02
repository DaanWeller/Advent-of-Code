def main():
    f = open("2024/day1/input_eva.txt")
    print("Using file " + f.name)
    lines = f.readlines()
    
    left_nums = []
    right_nums = []

    for line in lines:
        numbers = line.split()
        left_nums.append(numbers[0])
        right_nums.append(numbers[1])
    
    left_nums.sort()
    right_nums.sort()

    diff = 0
    for i in range(0, len(left_nums)):
        diff += abs(int(left_nums[i]) - int(right_nums[i]))

    print(diff)
    return 0


if __name__ == "__main__":
    main()