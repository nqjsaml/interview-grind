class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # something like this would be just
        # basic dfs and backtracking
        # but we can start anywhere with gold, so...?
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, total: int) -> int:
            # boundary condition or zero in cell
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return total
            # backtracking: store value of cell
            temp = grid[x][y]
            total += temp
            grid[x][y] = 0
            # recurse via dfs, we want to return this value
            ret = max(
                dfs(x+1, y, total),
                dfs(x-1, y, total),
                dfs(x, y+1, total),
                dfs(x, y-1, total)
            )
            # done with this cell, return the value to what it was
            grid[x][y] = temp
            return ret
        
        # now find a good place to start with gold
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j, 0))
        return ans
