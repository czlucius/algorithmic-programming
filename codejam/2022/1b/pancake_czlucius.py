
import math
from collections import deque
     

"""
Python template for Google Code Jam (non-interactive)
https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d
"""

# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    # print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass

testCases = int(input())

for testCase in range(1, testCases + 1):

    # Declaring deque
    numCakes = int(input())
    theList = [int(x) for x in input().split()]
    queue = deque(theList) 
    maxq  = max(queue)
    maxqnos = queue.count(maxq)
    payingCust = 0
    prevDeli = 0

    for q in range(numCakes):    
        
        first = queue[0]
        last = queue[-1]
        debug("f l ", first, last)



        if first > last and last >= prevDeli:
            # pop last cake.
            currentDeli = queue[-1]
            queue.pop()
        elif first > last:
            # do first.
            currentDeli = queue[0]
            queue.popleft()
            
        elif last > first and first >= prevDeli:
            #pop 1st cake
            currentDeli = queue[0]
            queue.popleft()
        else:
            currentDeli = queue[-1]
            queue.pop()
        

    
        debug("current prev", currentDeli, prevDeli)
        debug("queue", queue)

        if currentDeli ==  maxq:
            # no more paying cust.
            toaddpaying = maxqnos
            payingCust += toaddpaying
            break

        if prevDeli <= currentDeli:
            payingCust += 1

            prevDeli = currentDeli
            # Threshold, DELETE ALL in queue that is below this threshold. which is currentdeli
            qe = queue
            qz = [x for x in qe if x >= currentDeli]
            queue = deque(qz)
        
    
    answer = payingCust

    
    
    # answer = 0 # Please modify this to be whatever answer obtained.
    print(f"Case #{testCase}: {answer}")
