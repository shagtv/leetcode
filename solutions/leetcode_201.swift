class Solution {
    func rangeBitwiseAnd(_ left: Int, _ right: Int) -> Int {
        var left = left
        var right = right
        var shift = 0
        while left > 0 && left < right {
            left >>= 1
            right >>= 1
            shift += 1
        }
        return left << shift
    }
}


let given_left = 1
let given_right = 2147483647
let expected = 0

let solution = Solution()
let result = solution.rangeBitwiseAnd(given_left, given_right)
if result != expected {
    print("\(result) not equals \(expected)")
}
