import sys
from functools import cache


class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, 101)]

        @cache
        def helper(num):
            if num == 0:
                return 0
            return min(1 + helper(num - square) for square in squares if square <= num)

        return helper(n)


if __name__ == '__main__':
    given_n = 99
    expected = 3

    solution = Solution()
    result = solution.numSquares(given_n)
    assert result == expected
