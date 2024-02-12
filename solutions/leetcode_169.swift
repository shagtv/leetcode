class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        let half = nums.count / 2
        var counts = [Int: Int]()
        for num in nums {
            if counts[num] != nil {
                counts[num]! += 1
            } else {
                counts[num] = 1
            }
            if counts[num]! > half {
                return num
            }
        }
        return 0
    }
}
