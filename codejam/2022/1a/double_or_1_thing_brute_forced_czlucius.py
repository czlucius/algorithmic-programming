
import numpy as np
import math
from itertools import combinations, combinations_with_replacement
"""
Python template for Google Code Jam (non-interactive)
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c
"""
# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    # print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass

testCases = int(input())

for testCase in range(1, testCases + 1):
    
    stringS = input()
    debug(stringS)
    
    possibleArrangements = []
    for i in range(0, len(stringS) + 0):
        
        try:
            str0toMaxLen = "".join([str(x) for x in range(len(stringS))])
            debug(str0toMaxLen)
            possibleArrangements.extend(combinations(str0toMaxLen, i))
        except:
            break
    debug(possibleArrangements)
    
    possibleHighlighted = []
    for highlighted in possibleArrangements:
        new =""
        count = 0
        for char in stringS:
            if str(count) in highlighted:
                new +=char
                new += char
            else:
                new += char
            count += 1
        possibleHighlighted.append(new)
    
    debug(possibleHighlighted)
    possibleHighlighted.sort()
    answer = possibleHighlighted[0]
    
    
    print(f"Case #{testCase}: {answer}")
