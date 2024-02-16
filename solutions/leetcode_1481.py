class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        counts = sorted(counts.values())

        for i, count in enumerate(counts):
            if k >= count:
                k -= count
            else:
                return len(counts) - i
        return 0


if __name__ == '__main__':
    given_arr = [4, 3, 1, 1, 3, 3, 2]
    given_k = 3
    expected = 2

    solution = Solution()
    result = solution.findLeastNumOfUniqueInts(given_arr, given_k)
    assert result == expected
