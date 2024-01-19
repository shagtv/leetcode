from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = Counter(s)
        for c in t:
            if c not in chars or chars[c] == 0:
                return c
            chars[c] -= 1
        return ''


if __name__ == '__main__':
    given_s = "abcd"
    given_t = "abcde"
    expected = "e"

    solution = Solution()
    result = solution.findTheDifference(given_s, given_t)
    assert result == expected
