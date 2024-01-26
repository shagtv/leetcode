from functools import cache


class Solution:
    @cache
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startColumn < 0 or startRow == m or startColumn == n:
            return 1
        if maxMove == 0:
            return 0
        result = self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) + \
                 self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) + \
                 self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) + \
                 self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
        return result % 1_000_000_007


if __name__ == '__main__':
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    expected = 6

    solution = Solution()
    result = solution.findPaths(m, n, maxMove, startRow, startColumn)
    assert result == expected
