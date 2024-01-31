/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize){
    *returnSize = temperaturesSize;
    int *result = malloc(temperaturesSize * sizeof(int));
    int s[100];
    int top = 0;
    for (int i = temperaturesSize - 1; i >= 0; i--) {
        while (top > 0 && temperatures[i] >= temperatures[s[top - 1]]) {
            top--;
        }
        result[i] = top ? s[top - 1] - i : 0;
        s[top++] = i;
    }
    return result;
}