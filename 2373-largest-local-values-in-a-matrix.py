class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # is this really that simple?
        # think maximum pooling.
        n = len(grid)
        # ans = [[0] * (n-2) for _ in range(n-2)]
        # now iterate through each 3x3 grid
        # can be done as below (not in-place)
        """
        for i in range(n-2):
            for j in range(n-2):
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        ans[i][j] = max(ans[i][j], grid[x][y])
        return ans
        """
        # here, let's see the comparison with in-place
        # grid modification (@gameboey)
        for i in range(1, n-1):
            for j in range(1, n-1):
                t = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        t = max(t, grid[x][y])
                # here, we modify the previous space (up-left)
                # with the correct max value
                grid[i-1][j-1] = t
        # since we only touched non-boundary cells
        # trim them from the grid
        grid = [row[:n-2] for row in grid[:n-2]]
        return grid
