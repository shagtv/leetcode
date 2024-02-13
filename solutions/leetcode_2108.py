class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def is_poly_best(s):
            return s == s[::-1]

        def is_poly_by_chars(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        def is_poly_recursion(s):
            if len(s) <= 1:
                return True
            return s[0] == s[-1] and is_poly_recursion(s[1:len(s) - 1])

        for word in words:
            if is_poly_best(word):
                return word
        return ''


if __name__ == '__main__':
    given_words = ["abc", "car", "ada", "racecar", "cool"]
    expected = "ada"

    solution = Solution()
    result = solution.firstPalindrome(given_words)
    assert result == expected
