
calories_leaderboard = []
with open("day1.txt") as file:
    elves = file.read().split("\n\n")
    for elf in elves:
        list_of_nums = elf.splitlines()
        calories = 0
        for num in list_of_nums:
            calories += int(num)
        print(calories)
        calories_leaderboard.append(calories)
            
            
calories_leaderboard.sort()
print("Calories Leaderboard", calories_leaderboard)
print("Top 3 are carrying", calories_leaderboard[-1] + calories_leaderboard[-2] + calories_leaderboard[-3])