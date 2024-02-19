class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = 1
        while result < n:
            result *= 2
        return result == n


if __name__ == '__main__':
    given_n = 16
    expected = True

    solution = Solution()
    result = solution.isPowerOfTwo(given_n)
    assert result == expected
