class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = {}
        for winner, loser in matches:
            if winner not in players:
                players[winner] = 0
            players[loser] = players.get(loser, 0) + 1
        zeros = []
        ones = []
        for player in players:
            if players[player] == 0:
                zeros.append(player)
            elif players[player] == 1:
                ones.append(player)
        return [sorted(zeros), sorted(ones)]


if __name__ == '__main__':
    given_matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]

    solution = Solution()
    result = solution.findWinners(given_matches)
    assert result == expected
