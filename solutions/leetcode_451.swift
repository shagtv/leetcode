class Solution {
    func frequencySort(_ s: String) -> String {
        var dict = [Character:Int]()
        for c in s {
            dict[c] = dict[c, default:0] + 1
        }

        var list = [(Character,Int)]()
        for (c,count) in dict {
            list.append((c,count))
        }

        list.sort{a,b in
            a.1 > b.1
        }

        var result = ""
        for (c,count) in list {
            result += String(repeating: c, count: count)
        }

        return result
    }
}
