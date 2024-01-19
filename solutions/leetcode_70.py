from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    given_n = 3
    expected = 3

    solution = Solution()
    result = solution.climbStairs(given_n)
    assert result == expected
