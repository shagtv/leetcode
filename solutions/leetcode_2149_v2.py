class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        n, p = 1, 0
        for num in nums:
            if num < 0:
                result[n] = num
                n += 2
            else:
                result[p] = num
                p += 2
        return result


if __name__ == '__main__':
    given_nums = [3, 1, -2, -5, 2, -4]
    expected = [3, -2, 1, -5, 2, -4]

    solution = Solution()
    result = solution.rearrangeArray(given_nums)
    assert result == expected
