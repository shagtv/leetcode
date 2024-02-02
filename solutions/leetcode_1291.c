/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sequentialDigits(int low, int high, int* returnSize) {
    int n = 0;
    int f = 0;
    int num = low;
    *returnSize = 0;
    int* result = (int*)malloc(100 * sizeof(int));
    while (num) {
        n += 1;
        f = num % 10;
        num /= 10;
    }
    while (true) {
        if (f + n - 1 > 9) {
            n++;
            f = 1;
        }
        num = 0;
        for (int i = f; i < f + n; i++) {
            num = num * 10 + i;
        }
        if (num > high) break;
        if (num >= low) result[(*returnSize)++] = num;
        f++;
    }
    return result;
}
