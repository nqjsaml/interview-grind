class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # here, this is the choice of exactly ONE element in a row
        # that no two elements in adjacent rows are in the
        # same column
        # idea here is some dp
        n = len(grid)
        dp = [[-1] * n for _ in range(n)]
        # realize that we can go not strictly diagonally!
        ans = float('inf')
        # fill the first row with the values of grid, because this
        # is always gonna be part of the sum
        for j in range(n):
            dp[0][j] = grid[0][j]
        # begin dp: dp[i][j] is the falling sum in this column
        for i in range(1, n):
            for j in range(n):
                # current minimum sum up to this row
                cur = float('inf')
                # iterates through the columns again
                for k in range(n):
                    # avoids the same column
                    if j != k:
                        cur = min(cur, grid[i][j]+dp[i-1][k])
                dp[i][j] = cur
        # one of the answers is in the bottom row, so find the min
        # by iterating through that row
        for j in range(n):
            ans = min(ans, dp[n-1][j])
        return ans
