class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        mid = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid:
                return True
            while stack and stack[-1] < nums[i]:
                mid = stack.pop()
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    given_nums = [3,1,4,2]
    expected = True

    solution = Solution()
    result = solution.find132pattern(given_nums)
    assert result == expected
