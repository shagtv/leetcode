class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        for i, num in enumerate(nums):
            total_sum -= num
            if num < total_sum:
                if len(nums) - i < 3:
                    return -1
                return total_sum + num
        return -1


if __name__ == '__main__':
    given_nums = [1, 12, 1, 2, 5, 50, 3]
    expected = 12

    solution = Solution()
    result = solution.largestPerimeter(given_nums)
    assert result == expected
