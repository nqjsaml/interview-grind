class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this is probably some graph bfs. an island is surrounded by water
        # and is connected HORIZONTALLY or VERTICALLY by land tiles
        # basically, the number of connected components in a graph.
        ans = 0
        m, n = len(grid), len(grid[0])
        # the goal is this: iterate linearly through the grid and when we reach a '1', initiate bfs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.bfs(grid, i, j)
        return ans

    # this function here searches all neighbors of the current cell for land and considers them as an island
    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        q = collections.deque()
        q.append((i, j))
        while q:
            # (row, col) tuple
            x, y = q.popleft()
            # out of bounds, continue
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            # water cell, don't care
            if grid[x][y] == '0':
                continue
            # so we don't use extra space aside from recursion stack, mark visited cell as a water cell
            grid[x][y] = '0'
            # and bfs through neighbors (down -> up -> left -> right, order doesn't really matter)
            q.append((x+1, y))
            q.append((x-1, y))
            q.append((x, y-1))
            q.append((x, y+1))
