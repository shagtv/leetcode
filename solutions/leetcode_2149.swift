class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        var result = [Int]()
        for _ in 0..<nums.count {
            result.append(0)
        }
        var n = 1
        var p = 0
        for num in nums {
            if num < 0 {
                result[n] = num
                n += 2
            } else {
                result[p] = num
                p += 2
            }
        }
        return result
    }
}
