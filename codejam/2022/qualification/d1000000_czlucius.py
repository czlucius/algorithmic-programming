"""
Python template for Google Code Jam (non-interactive)
"""
# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    #print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass
testCases = int(input())
for testCase in range(1, testCases + 1):
    numDice = int(input())
    dices = [int(x) for x in input().split()]
    dices.sort()
    current = 1
    straight = 0
    # Always in ascending order.
    for dice in dices:
        debug("str", straight)
        debug("dice", dice, "current", current)
        if current > dice:
            # The current highest number in straight is higher than highest number of this dice. Abort.
            break
        if straight == dice:
            if current != dices[-1]:
                continue
            else:
                break
        straight += 1
        current = dice
    answer = str(straight) # Please modify this to be whatever answer obtained.
    print(f"Case #{testCase}: {answer}")