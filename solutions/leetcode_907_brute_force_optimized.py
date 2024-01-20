class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        result = 0
        n = len(arr)
        for i in range(n):
            min_val = arr[i]
            for j in range(i, n):
                min_val = min(min_val, arr[j])
                result += min_val
        return result % 1_000_000_007


if __name__ == '__main__':
    given_arr = [11, 81, 94, 43, 3]
    expected = 444

    solution = Solution()
    result = solution.sumSubarrayMins(given_arr)
    assert result == expected
