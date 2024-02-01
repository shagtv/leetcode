class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []
        nums.sort()
        result = []
        part = []
        for num in nums:
            part.append(num)
            if len(part) == 3:
                if part[2] - part[0] > k:
                    return []
                result.append(part)
                part = []
        return result


if __name__ == '__main__':
    given_nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    given_k = 2
    expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

    solution = Solution()
    result = solution.divideArray(given_nums, given_k)
    assert result == expected
