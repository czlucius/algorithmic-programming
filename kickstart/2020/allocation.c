#include<stdio.h>
#include<stdlib.h>
// https://zibada.guru/gcj/ks2020a/problems/

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


char* testCase(const int i) {
    // printf("%d", i);
    int length, B;
    scanf("%d %d", &length, &B);
    int items[length];
    for (int i=0;i<length;i++) {
        scanf("%d", &(items[i]));

    }

    //     for (int i=0;i<length;i++) {
    //     printf("item[%d]: %d", i, (items[i]));
    // }

    // Use a greedy approach
    // Take the lowest to highest
    // sizeof(int) for size of an int
    qsort(items, length, sizeof(int), cmpfunc);



    // pick smallest number 1st, then iteratively work your way.
    int sum = 0;
    int j = 0;
    int k = 0;
    for (j =0;j<length;j++) {
        int newsum = sum + items[j];
        // printf("%d %d %d %d %d -> ", sum, items[j], newsum, k, length);
        if (newsum > B) {
            break;
        } else {
            sum = newsum;
        }
        k++;
    }
    printf("%d", k);






    char* ans = "";
    return ans;

}


int main() {
    int testCases = 0;
    scanf("%d ", &testCases);
    // printf("test cases %d", testCases);
    for (int i=1; i<=testCases; i++) {
        printf("Case #%d: ", i);
        printf("%s", testCase(i));
        printf("\n");
    }

}





