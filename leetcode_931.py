from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        @cache
        def helper(col, row):
            if col < 0 or col == len(matrix[0]):
                return 1_000_000
            if row == len(matrix):
                return 0
            return matrix[row][col] + min(
                helper(col - 1, row + 1),
                helper(col, row + 1),
                helper(col + 1, row + 1)
            )
        return min(helper(col, 0)
            for col in range(len(matrix))
        )


if __name__ == '__main__':
    given_matrix = [[-19,57],[-40,-5]]
    expected = -59

    solution = Solution()
    result = solution.minFallingPathSum(given_matrix)
    assert result == expected
