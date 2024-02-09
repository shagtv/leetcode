from functools import cache


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()

        @cache
        def helper(i, prev):
            if i == len(nums):
                return []

            result = []
            for j in range(i, len(nums)):
                if nums[j] % prev == 0:
                    local_result = [nums[j]] + helper(j + 1, nums[j])
                    if len(local_result) > len(result):
                        result = local_result
            return result


        result = []
        for i in range(len(nums)):
            local_result = [nums[i]] + helper(i + 1, nums[i])
            if len(local_result) > len(result):
                result = local_result

        return result


if __name__ == '__main__':
    given_nums = [8, 4, 2, 1]
    expected = [1, 2, 4, 8]

    solution = Solution()
    result = solution.largestDivisibleSubset(given_nums)

    assert result == expected
