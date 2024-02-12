class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        half = len(nums) // 2
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > half:
                return num


if __name__ == '__main__':
    given_nums = [2, 2, 1, 1, 1, 2, 2]
    expected = 2

    solution = Solution()
    result = solution.majorityElement(given_nums)
    assert result == expected
