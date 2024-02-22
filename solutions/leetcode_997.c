#include  <stdlib.h>

int findJudge(int n, int** trust, int trustSize, int* trustColSize){
    if (n == 1) return 1;
    int16_t *votes = calloc(n + 1, sizeof(int16_t));
    for (int i = 0; i < trustSize; i++) {
        votes[trust[i][1]]++;
        votes[trust[i][0]]--;
    }
    for (int i = 1; i <= n; i++) {
        if (votes[i] == n - 1) {
            return i;
        }
    }
    free(votes);
    return -1;
}
