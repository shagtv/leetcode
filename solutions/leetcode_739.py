class Solution:
    def dailyTemperatures(self, temperatures:list[int]) -> list[int]:
        n = len(temperatures)
        answers = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                answers[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return answers


if __name__ == '__main__':
    given_temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]

    solution = Solution()
    result = solution.dailyTemperatures(given_temperatures)
    assert result == expected
