int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize)
{
    for (int row = 1; row < matrixSize; row++) {
        for (int col = 0; col < matrixSize; col++) {
            int min = matrix[row - 1][col];
            if (col - 1 >= 0 && matrix[row - 1][col - 1] < min)
                min = matrix[row - 1][col - 1];
            if (col + 1 < matrixSize && matrix[row - 1][col + 1] < min)
                min = matrix[row - 1][col + 1];
            matrix[row][col] += min;
        }
    }
    int min = INT_MAX;
    int row = matrixSize - 1;
    for (int col = 0; col < matrixSize; col++) {
        if (matrix[row][col] < min)
            min = matrix[row][col];
    }

    return min;
}
