"""
Python template for Google Code Jam (non-interactive)
"""

# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    # print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass

testCases = int(input())

for testCase in range(1, testCases + 1):
    
    rows, cols = [int(x) for x in input().split()]
    rows = rows+1
    ans = ""
    
    for row in range(rows - 1):
        
        artOnRow = ["+-" for x in range(cols)]
        artOnRow.append("+")
        sepRow = ["|." for x in range(cols)]
        sepRow.append("|")
        if row == 0:
            artOnRow[0:1] = [".","."]
            sepRow[0:1] = [".", "."]
        
        ans += "".join(artOnRow)
        ans += "\n"
        ans += "".join(sepRow)
        ans += "\n"
    
    ans += ("+-" * cols) # Add last row.
    ans += "+"
 
    print(f"Case #{testCase}:")
    print(ans)