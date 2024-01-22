class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s = set()
        twice = None
        for num in nums:
            if num in s:
                twice = num
            s.add(num)
        missed = None
        for i in range(1, len(nums) + 1):
            if i not in s:
                missed = i
                break
        return [twice, missed]


if __name__ == '__main__':
    given_nums = [1, 2, 2, 4]
    expected = [2, 3]

    solution = Solution()
    result = solution.findErrorNums(given_nums)
    assert result == expected
