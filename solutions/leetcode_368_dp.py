class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()

        result = [nums[0]]
        dp = [[num] for num in nums]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    dp[j] = [nums[j]] + dp[i]
                    if len(dp[j]) > len(result):
                        result = dp[j]
        return result


if __name__ == '__main__':
    given_nums = [8, 4, 2, 1]
    expected = {1, 2, 4, 8}

    solution = Solution()
    result = solution.largestDivisibleSubset(given_nums)

    assert set(result) == expected
