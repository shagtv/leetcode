class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        low_s = str(low)
        n = len(low_s)
        first = int(low_s[0])
        while True:
            if first + n - 1 > 9:
                first = 1
                n += 1
            num = 0
            for i in range(first, first + n):
                num = num * 10 + i
            if num > high:
                break
            if num >= low:
                result.append(num)
            first += 1

        return result


if __name__ == '__main__':
    given_low = 1000
    given_high = 13000
    expected = [1234, 2345, 3456, 4567, 5678, 6789, 12345]

    solution = Solution()
    result = solution.sequentialDigits(given_low, given_high)
    assert result == expected
