/**
C++ template for Google Code Jam (non-interactive)
*/
#include <iostream>
// #ifndef GOOGLE_CODE_JAM

/**
 * Use to debug your code.
 * Use like cout, like this:
 * debug << "Some text";
 * debug << someVar;
 * 
 * To disable the log statements, change 
 * #if 1
 * to:
 * #if 0
 */
#if 1
#define debug cout
#else
#define debug 0 && cout
#endif

using namespace std;



int main()
{
    // Multiple test cases will be supplied. Read from testCases to get no. of testCases
    int testCases; cin >> testCases;
    
    for (int i = 1; i <= testCases; i++) {
        // Do your code every test case here.
        
        
        auto answer = 99; // Please modify this to be whatever answer obtained.
        cout << "Case #" << i << ": " << answer << endl;
    }
    
    return 0;
}
