class Solution {
    func findJudge(_ n: Int, _ trust: [[Int]]) -> Int {
        if n == 1 { return 1 }
        var voters: [Int] = Array(repeating: 0, count: n + 1)
        var votees: [Int] = Array(repeating: 0, count: n + 1)
        for vote in trust {
            voters[vote[0]] = 1
            votees[vote[1]] += 1
        }

        for voteeId in 1..<votees.count {
            if voters[voteeId] == 0 && votees[voteeId] == n - 1 {
                return voteeId
            }
        }

        return -1
    }
}

let givenN = 3
let givenTrust: [[Int]] = [[1, 3], [2, 3], [3, 1]]
let expected = -1

let solution = Solution()
let result = solution.findJudge(givenN, givenTrust)
if result != expected {
    print("\(result) not equals \(expected)")
}
