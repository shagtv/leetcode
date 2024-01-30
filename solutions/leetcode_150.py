class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-/*':
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == '__main__':
    given_tokens = ["2", "1", "+", "3", "*"]
    expected = 9

    solution = Solution()
    result = solution.evalRPN(given_tokens)
    assert result == expected
