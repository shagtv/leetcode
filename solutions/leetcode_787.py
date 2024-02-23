from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for frm, to, price in flights:
            d[frm].append((to, price))
        q = [(src, 0)]
        seen = {src: 0}
        result = float('inf')
        while q and k >= 0:
            k -= 1
            new_q = []
            while q:
                src, total = q.pop()
                for to, price in d[src]:
                    price += total
                    if to == dst:
                        result = min(result, price)
                    if to not in seen or seen[to] > price:
                        seen[to] = price
                        new_q.append((to, price))
            q = new_q
        return result if result != float('inf') else -1


if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    expected = 700

    solution = Solution()
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert result == expected
