class Solution {
    func numSquares(_ n: Int) -> Int {
        var result = 0
        var squares = [Int]()
        for i in 1...100 {
            squares.append(i*i)
        }

        var q = Set<Int>()
        q.insert(n)
        while !q.isEmpty {
            result += 1
            var newQ = Set<Int>()
            while !q.isEmpty {
                let cur = q.removeFirst()
                for i in squares {
                    let val = cur - i
                    if val == 0 {
                        return result
                    } else if (val > 0) {
                        newQ.insert(val)
                    }
                }
            }
            q = newQ
        }

        return result
    }
}
