"""
Saving the Universe
Google Code Jam 2008
By @czlucius
"""
# Use to debug your code. 
# Use it like print, it will pass all arguments to print (including positional args so you do not have to concatenate and convert values)
def debug(vals, *pvals, **kwvals):
    # print(vals, *pvals, **kwvals) # Comment this out when doing actual run (so this fn results in no-op). For printing of debug statements.
    pass

def submit(testCase, answer):
    print(f"Case #{testCase}: {answer}")

testCases = int(input())

for testCase in range(1, testCases + 1):

    numEngines = int(input())
    engines = {} # Use (hash) dict for fast execution.
    for i in range(numEngines):
        engine = input()
        engines[engine] = engine
    
    numQueries = int(input())
    queries = []

    for i in range(numQueries):
        query = input()
        # ALL queries are valid search engines.
        assert engines[query] != None # O(1)
        queries.append(query)
        

    qSet = set(queries) #O(n) only.
    if len(qSet) < numEngines:
        # Some engines unused.
        # Zero switches. answer = 0
        submit(testCase, 0)
        continue
    
    # Which engine has the highest no bef rate?
    queryEngineCount = {}
    switches = 0
    
    for q in queries:
        debug("qec", queryEngineCount, "sw", switches, "q", q)
        if q not in queryEngineCount and len(queryEngineCount) == numEngines - 1:
            # Last engine to be used. Use this until 
            switches += 1
            queryEngineCount = {} # reset queryEngineCount
        
        
        
        
        if q not in queryEngineCount:
            queryEngineCount[q] = 1
        else:
            queryEngineCount[q] += 1
        
    
    
    

    
    
    submit(testCase, switches)
