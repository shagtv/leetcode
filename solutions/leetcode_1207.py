from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        s = set()
        for i in Counter(arr).values():
            if i in s:
                return False
            s.add(i)
        return True


if __name__ == '__main__':
    given_arr = [1,2,2,1,1,3]
    expected = True

    solution = Solution()
    result = solution.uniqueOccurrences(given_arr)
    assert result == expected
