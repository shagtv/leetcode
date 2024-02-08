class Solution:
    def numSquares(self, n: int) -> int:
        result = 0
        squares = [i * i for i in range(100, 0, -1)]
        q = {n}
        while q:
            result += 1
            new_q = set()
            while q:
                cur = q.pop()
                for i in squares:
                    if cur - i == 0:
                        return result
                    elif cur - i > 0:
                        new_q.add(cur - i)
            q = new_q
        return result


if __name__ == '__main__':
    given_n = 9999
    expected = 4

    solution = Solution()
    result = solution.numSquares(given_n)
    assert result == expected
