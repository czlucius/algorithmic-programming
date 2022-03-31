"""
Reverse sort for Google Code Jam 2021.

 L=[4,2,1,3]
 
 i = 1
 we would get:
 j = 3
 
 and it does:
 
 4, 2, 1, 3
    |
    v
 (flips the 4, 2, 1 (only up to j) to 1, 2, 4)
 1, 2, 4, 3
 
 L = [1, ||2, 4, 3]||
 i = 2
 we get j = 2 as we only look @ 2nd elem onwards.
 j = 2. because the 2nd no is the smallest.
 
 2,4,3
 supplies to RS 2..2 which is nothing.
 
 L = [1, 2, ||4, 3]||
 i = 3
 j = 4
 4,3
 |
 v
 3,4
 
 
 
"""


def revlist(lis):
    return list(reversed(lis))

def debug(value, *ovals, **kwvals):
    #print(value, ovals, kwvals)
    pass


numCases = int(input())

for case in range(numCases):
    listLen = int(input())
    sList = [int(i) for i in input().split()]
    debug("sList", sList)
    
    iters = listLen - 1
    costEach = 0 
    
    for i in range(1, iters+1):
        i0 = i - 1
        
        moddedSList = sList[i0:]
        index_min = min(range(len(moddedSList)), key=moddedSList.__getitem__)
        j = index_min + i
        debug("j="+str(j))
        j0 = j - 1
        costEach += (j-i+1)
        debug(costEach)
        torev = sList[i0:j]
        debug(torev)
        reversal = revlist(torev)
        
        sList = sList[:i0] + reversal + sList[j:]
    print(f"Case #{case + 1}: {costEach}")
        
