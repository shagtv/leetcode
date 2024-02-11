from functools import cache


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        @cache
        def helper(x1, x2, y):
            if x1 < 0 or x1 >= len(grid[0]): return 0
            if x2 < 0 or x2 >= len(grid[0]): return 0
            if y >= len(grid): return 0
            if x1 == x2: return 0

            result = 0
            for x1_diff in (-1, 0, 1):
                for x2_diff in (-1, 0, 1):
                    result = max(result, helper(x1 + x1_diff, x2 + x2_diff, y + 1))
            return result + grid[y][x1] + grid[y][x2]

        return helper(0, len(grid[0]) - 1, 0)


if __name__ == '__main__':
    given_grid = [[3, 1, 1], [2, 5, 1],[1, 5, 5],[2, 1, 1]]
    expected = 24

    solution = Solution()
    result = solution.cherryPickup(given_grid)
    assert result == expected
