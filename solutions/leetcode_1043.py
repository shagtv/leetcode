from functools import cache


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        @cache
        def helper(start):
            result = 0
            max_sum = 0
            for i in range(k):
                if start + i < len(arr):
                    max_sum = max(max_sum, arr[start + i])
                    result = max(result, max_sum * (i + 1) + helper(start + i + 1))

            return result

        return helper(0)


if __name__ == '__main__':
    given_arr = [1, 15, 7, 9, 2, 5, 10]
    given_k = 3
    expected = 84

    solution = Solution()
    result = solution.maxSumAfterPartitioning(given_arr, given_k)
    assert result == expected
