class Solution:
    def maxLength(self, arr: list[str]) -> int:
        arr = [set(s) for s in arr if len(set(s)) == len(s)]

        def helper(i, s):
            if i == len(arr):
                return len(s)
            return max(
                helper(i + 1, s),
                0 if s & arr[i] else helper(i + 1, s | arr[i]),
            )

        return helper(0, set())


if __name__ == '__main__':
    given_arr = ["cha", "r", "act", "ers"]
    expected = 6

    solution = Solution()
    result = solution.maxLength(given_arr)
    assert result == expected
