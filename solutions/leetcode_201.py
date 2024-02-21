class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while 0 < left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


if __name__ == '__main__':
    given_left = 1
    given_right = 2147483647
    expected = 0

    solution = Solution()
    result = solution.rangeBitwiseAnd(given_left, given_right)
    assert result == expected
