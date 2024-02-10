class Solution {
    func largestDivisibleSubset(_ nums: [Int]) -> [Int] {
        var nums = nums.sorted()
        var dp = [[Int]]()
        for num in nums {
            dp.append([num])
        }

        for i in 0..<(nums.count - 1) {
            for j in (i + 1)..<nums.count {
                if nums[j] % nums[i] == 0 {
                    if dp[i].count + 1 > dp[j].count {
                        dp[j] = [nums[j]] + dp[i]
                    }
                }
            }
        }

        var index = 0
        for i in 1..<dp.count {
            if dp[i].count > dp[index].count {
                index = i
            }
        }

        return dp[index]
    }
}
