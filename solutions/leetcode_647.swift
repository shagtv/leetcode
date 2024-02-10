class Solution {
    func helper(_ l:Int, _ r:Int, _ chars:[Character]) -> Int {
        var result = 0
        var l = l
        var r = r
        while l >= 0 && r < chars.count && chars[l] == chars[r] {
            result += 1
            l -= 1
            r += 1
        }
        return result
    }

    func countSubstrings(_ s: String) -> Int {
        var result = 0
        let chars = Array(s)
        for i in 0..<s.count {
            result += helper(i, i, chars)
            result += helper(i, i + 1, chars)
        }
        return result
    }
}
