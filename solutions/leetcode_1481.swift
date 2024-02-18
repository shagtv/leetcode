class Solution {
    func findLeastNumOfUniqueInts(_ arr: [Int], _ k: Int) -> Int {
        var counts:[Int:Int] = [:]
        for num in arr {
            if counts[num] ==  nil {
                counts[num] = 0
            }
            counts[num] = counts[num]! + 1
        }

        var values: [Int] = counts.values.sorted()
        var k = k
        for i in 0..<values.count {
            if k >= values[i] {
                k -= values[i]
            } else {
                return values.count - i
            }
        }

        return 0
    }
}
