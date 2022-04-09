
"""
Python template for Google Code Jam (non-interactive)
"""
import numpy as np
# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass

tenE6 = 1000000
testCases = int(input())

for testCase in range(1, testCases + 1):
    
    # [0] is c, [1] is m, [2] is y, [3] is k
    p1 = [int(x) for x in input().split()]
    p2 = [int(x) for x in input().split()]
    p3 = [int(x) for x in input().split()]
    
    pa = np.array([p1, p2, p3])
    ptrans = pa.T
    
    # Each image MUST be made out of 10^6 of ink.
    
    totalUsed = 0
    ans = [0,0,0,0]
    for color in [0,1,2,3]:
        # Use the min of the 3 printers
        amount = min(ptrans[color])
        arctu = totalUsed
        totalUsed += amount
        debug(totalUsed)
        ans[color] = amount

        if totalUsed > tenE6:
            # Deduct amount until totalUsed = tenE6
            diff = totalUsed - tenE6
            amount -= diff
            totalUsed = arctu + amount
            ans[color] = amount

            break
        elif totalUsed == tenE6:
            break
        
        debug("color", color)
        
    
    if totalUsed == tenE6:
        ansStr = ""
        for col in ans:
            ansStr += str(col)
            ansStr += " "
    else:
        ansStr = "IMPOSSIBLE"
    
    
    print(f"Case #{testCase}: {ansStr}")