from functools import cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def helper(start):
            if start >= len(nums):
                return 0
            return max(
                nums[start] + helper(start + 2),
                helper(start + 1)
            )
        return helper(0)


if __name__ == '__main__':
    given_nums = [2, 7, 9, 3, 1]
    expected = 12

    solution = Solution()
    result = solution.rob(given_nums)
    assert result == expected
