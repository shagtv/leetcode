class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        voters = [0] * (n + 1)
        votees = [0] * (n + 1)
        for voter, votee in trust:
            voters[voter] = 1
            votees[votee] += 1
        for votee, votes in enumerate(votees):
            if not voters[votee] and votes == n - 1:
                return votee
        return -1


if __name__ == '__main__':
    given_n = 3
    given_trust = [[1, 3], [2, 3], [3, 1]]
    expected = -1

    solution = Solution()
    result = solution.findJudge(given_n, given_trust)
    if result != expected:
        print(result, "not equals", expected)
