class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            result = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            return result

        result = 0
        for start in range(len(s)):
            result += helper(start, start)
            result += helper(start, start + 1)
        return result



if __name__ == '__main__':
    given_s = "aaa"
    expected = 6

    solution = Solution()
    result = solution.countSubstrings(given_s)
    assert result == expected
