class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    continue
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    result += 1
        return result


if __name__ == '__main__':
    given_s = "aaa"
    expected = 6

    solution = Solution()
    result = solution.countSubstrings(given_s)
    assert result == expected
