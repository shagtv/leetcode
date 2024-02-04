from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        t_len = len(t)
        l, r = 0, 0
        found = False
        while t and r < len(s):
            if s[r] in t:
                t[s[r]] -= 1
                if not t[s[r]]:
                    t_len -= 1
                    if t_len == 0:
                        found = True
                        break
            r += 1
        if not found:
            return ''
        min_len = r + 1
        min_result = s[l:r + 1]
        while l < len(s):
            moved = False
            while l < len(s) - 1 and (s[l] not in t or t[s[l]] < 0):
                if s[l] in t:
                    t[s[l]] += 1
                l += 1
                moved = True
            cur_min = r - l + 1
            if cur_min < min_len:
                min_result = s[l:r + 1]
                min_len = cur_min
            if r < len(s) - 1:
                r += 1
                if s[r] in t:
                    t[s[r]] -= 1
                moved = True
            if not moved:
                break

        return min_result


if __name__ == '__main__':
    given_s = 'ADOBECODEBANC'
    given_t = 'ABC'
    expected = 'BANC'

    solution = Solution()
    result = solution.minWindow(given_s, given_t)
    assert result == expected
