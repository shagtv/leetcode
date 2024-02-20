class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        var sum = 0
        for i in 0...nums.count {
            sum += i
        }
        for num in nums {
            sum -= num
        }
        return sum
    }
}


let given_nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
let expected = 8

let solution = Solution()
let result = solution.missingNumber(given_nums)
if result != expected {
    print("\(result) not equals \(expected)")
}
