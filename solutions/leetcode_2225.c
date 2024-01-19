/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findWinners(int** matches, int matchesSize, int* matchesColSize, int* returnSize, int** returnColumnSizes){
    #define MAX 100001
    int players[MAX];
    memset(players, -1, MAX * sizeof(int));

    int *columnSizes = malloc(2 * sizeof(int));
    columnSizes[0] = 0;
    columnSizes[1] = 0;

    for (int i = 0; i < matchesSize; i++) {
        if (players[matches[i][1]] == -1) {
            players[matches[i][1]] = 1;
            columnSizes[1] += 1;
        } else {
            if (players[matches[i][1]] == 0) {
                columnSizes[0] -= 1;
                columnSizes[1] += 1;
            } else if (players[matches[i][1]] == 1) {
                columnSizes[1] -= 1;
            }

            players[matches[i][1]] += 1;
        }

        if (players[matches[i][0]] == -1) {
            columnSizes[0] += 1;
            players[matches[i][0]] = 0;
        }
    }

    int *no_lose = malloc(columnSizes[0] * sizeof(int));
    int *one_lose = malloc(columnSizes[1] * sizeof(int));

    int ii = 0, jj = 0;
    for (int i = 0; i < MAX; i++) {
        if (players[i] == 0) {
            no_lose[ii++] = i;
        } else if (players[i] == 1) {
            one_lose[jj++] = i;
        }
    }

    *returnColumnSizes = columnSizes;
    *returnSize = 2;

    int **result = malloc(2 * sizeof(int*));
    result[0] = no_lose;
    result[1] = one_lose;

    return result;
}
