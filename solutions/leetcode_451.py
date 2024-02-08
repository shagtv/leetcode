class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        chars = sorted(chars.items(), key=lambda k:k[1], reverse=True)
        return ''.join(c*count for c,count in chars)


if __name__ == '__main__':
    given_n = "tree"
    expected = "eetr"

    solution = Solution()
    result = solution.frequencySort(given_n)
    assert result == expected
