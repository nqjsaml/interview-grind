class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # just a very formulaic thing ig
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # we only care if the cell is a land cell so
                if grid[i][j] == 1:
                    # start with adding 4 for now
                    ans += 4
                    # right OR down is land so total contribution is 2 due to shared side
                    if i < m-1 and grid[i+1][j] == 1:
                        ans -= 2
                    if j < n-1 and grid[i][j+1] == 1:
                        ans -= 2
        return ans
