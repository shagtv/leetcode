from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        d = defaultdict(dict)
        secret = {0, firstPerson}
        for x, y, t in meetings:
            if x not in d[t]:
                d[t][x] = set()
            d[t][x].add(y)
            if y not in d[t]:
                d[t][y] = set()
            d[t][y].add(x)
        d = sorted(d.items(), key=lambda k: k[0])

        for _, pairs in d:
            for x in pairs:
                if x in secret:
                    q = [x]
                    while q:
                        new_q = []
                        while q:
                            new_x = q.pop()
                            for y in pairs[new_x]:
                                if y not in secret:
                                    secret.add(y)
                                    new_q.append(y)
                        q = new_q

        return list(secret)


if __name__ == '__main__':
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    expected = [0, 1, 2, 3, 5]

    solution = Solution()
    result = solution.findAllPeople(n, meetings, firstPerson)
    assert result == expected
