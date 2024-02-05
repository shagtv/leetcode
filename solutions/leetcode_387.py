from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    given_s = "loveleetcode"
    expected = 2

    solution = Solution()
    result = solution.firstUniqChar(given_s)
    assert result == expected
