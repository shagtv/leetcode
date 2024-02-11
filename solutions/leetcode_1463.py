from functools import cache


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        @cache
        def helper(y1, x1, y2, x2):
            if not 0 <= x1 < len(grid[0]) \
                    or not 0 <= y1 < len(grid) \
                    or not 0 <= x2 < len(grid[0]) \
                    or not 0 <= y2 < len(grid) \
                    or x1 == x2 and y1 == y2:
                return 0

            return grid[y1][x1] + grid[y2][x2] + max(
                helper(y1 + 1, x1 - 1, y2 + 1, x2 - 1),
                helper(y1 + 1, x1 - 1, y2 + 1, x2),
                helper(y1 + 1, x1 - 1, y2 + 1, x2 + 1),
                helper(y1 + 1, x1, y2 + 1, x2 - 1),
                helper(y1 + 1, x1, y2 + 1, x2),
                helper(y1 + 1, x1, y2 + 1, x2 + 1),
                helper(y1 + 1, x1 + 1, y2 + 1, x2 - 1),
                helper(y1 + 1, x1 + 1, y2 + 1, x2),
                helper(y1 + 1, x1 + 1, y2 + 1, x2 + 1)
            )

        return helper(0, 0, 0, len(grid[0]) - 1)


if __name__ == '__main__':
    given_grid = [[3, 1, 1], [2, 5, 1],[1, 5, 5],[2, 1, 1]]
    expected = 24

    solution = Solution()
    result = solution.cherryPickup(given_grid)
    assert result == expected
