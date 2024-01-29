from collections import defaultdict


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d = defaultdict(int)
        d[(startRow, startColumn)] = 1
        steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        result = 0
        while maxMove >= 0:
            new_d = defaultdict(int)
            maxMove -= 1
            for (row, col), count in d.items():
                if 0 <= row < m and 0 <= col < n:
                    for dr, dc in steps:
                        new_d[(row + dr, col + dc)] += count
                else:
                    result += count
            d = new_d
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
