from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if text1[i1] == text2[i2]:
                return 1 + helper(i1 + 1, i2 + 1)
            else:
                return max(
                    helper(i1, i2 + 1),
                    helper(i1 + 1, i2)
                )

        return helper(0, 0)


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    expected = 3

    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    assert result == expected
