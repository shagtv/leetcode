class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        var total_sum = nums.reduce(0, +)
        let nums = Array(nums.sorted().reversed())
        for i in 0..<nums.count {
            total_sum -= nums[i]
            if nums[i] < total_sum {
                if nums.count - i < 3 {
                    return -1
                }
                return total_sum + nums[i]
            }
        }
        return -1
    }
}
