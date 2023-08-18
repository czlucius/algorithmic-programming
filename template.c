#include<stdio.h>


char* testCase(int i) {
    // printf("%d", i);

    char* ans = "hello";
    return ans;

}


int main() {
    int testCases = 0;
    scanf("%d ", &testCases);
    // printf("test cases %d", testCases);
    for (int i=1; i<=testCases; i++) {
        printf("Test case %d: %s\n", i, testCase(i));
    }

}





