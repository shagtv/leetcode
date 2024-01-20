class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        left, right, stack = [0] * n, [0] * n, []
        for i in range(n):
            count = 1
            while stack and arr[i] < stack[-1][0]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and arr[i] <= stack[-1][0]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count
        return sum(arr[i] * left[i] * right[i] for i in range(n)) % 1_000_000_007


if __name__ == '__main__':
    given_arr = [11, 81, 94, 43, 3]
    expected = 444

    solution = Solution()
    result = solution.sumSubarrayMins(given_arr)
    assert result == expected
