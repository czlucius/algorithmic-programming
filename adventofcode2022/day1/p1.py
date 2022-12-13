highest_calorie = 0
with open("day1.txt") as file:
    elves = file.read().split("\n\n")
    print(elves)
    for elf in elves:
        list_of_nums = elf.splitlines()
        calories = 0
        for num in list_of_nums:
            calories += int(num)
            
        if calories > highest_calorie:
            highest_calorie = calories
            
            
print("Most calories:", highest_calorie)