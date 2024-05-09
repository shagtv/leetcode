class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        fee = 0
        result = 0
        for h in happiness:
            h -= fee
            if h <= 0:
                break
            result += h
            fee += 1
            if fee == k:
                break
        return result
