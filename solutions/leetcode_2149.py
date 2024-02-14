class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = []
        p, n = 0, 0
        while p < len(nums) and n < len(nums):
            while nums[p] < 0:
                p += 1
            result.append(nums[p])
            while nums[n] > 0:
                n += 1
            result.append(nums[n])
            p += 1
            n += 1
        return result


if __name__ == '__main__':
    given_nums = [3, 1, -2, -5, 2, -4]
    expected = [3, -2, 1, -5, 2, -4]

    solution = Solution()
    result = solution.rearrangeArray(given_nums)
    assert result == expected
