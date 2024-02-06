class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var d:[String:[String]] = [:]
        for str in strs {
            let sortedStr = String(str.sorted())
            d[sortedStr, default: []].append(str)
        }
        return Array(d.values)
    }
}
