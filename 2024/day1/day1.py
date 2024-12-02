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
    similarity = 0
    for i in range(0, len(left_nums)):
        diff += abs(int(left_nums[i]) - int(right_nums[i]))
        similarity += int(left_nums[i]) * right_nums.count(left_nums[i])



    print("The answer to part 1 is " + str(diff))
    print("The answer to part 2 is " + str(similarity))

    return 0


if __name__ == "__main__":
    main()