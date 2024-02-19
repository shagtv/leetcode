class Solution {
    func isPowerOfTwo(_ n: Int) -> Bool {
        var result = 1
        while result < n {
            result *= 2
        }
        return result == n
    }
}
