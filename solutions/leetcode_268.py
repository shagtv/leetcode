class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    given_nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected = 8

    solution = Solution()
    result = solution.missingNumber(given_nums)
    assert result == expected
