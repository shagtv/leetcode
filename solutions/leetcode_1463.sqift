struct Triple: Hashable {
    let x1: Int
    let x2: Int
    let y: Int
}

class Solution {
    var grid = [[Int]]()
    var cache = [Triple: Int]()

    func helper(_ x1: Int, _ x2: Int,  _ y: Int) -> Int {
        let key = Triple(x1:x1, x2: x2, y:y)
        if let cacheResult = cache[key] {
            return cacheResult
        }

        guard x1 >= 0 && x1 < grid[0].count else { return 0 }
        guard x2 >= 0 && x2 < grid[0].count else { return 0 }
        guard y < grid.count else { return 0 }
        guard x1 != x2 else { return 0 }

        var result = 0
        for x1Diff in [-1, 0, 1] {
            for x2Diff in [-1, 0, 1] {
                result = max(result, helper(x1 + x1Diff, x2 + x2Diff, y + 1))
            }
        }

        result += grid[y][x1] + grid[y][x2]
        cache[key] = result

        return result
    }

    func cherryPickup(_ grid: [[Int]]) -> Int {
        self.grid = grid
        return helper(0, grid[0].count - 1, 0)
    }
}
