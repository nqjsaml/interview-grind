class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # recall that every row represents a NUMBER
        ans = 0
        m, n = len(grid), len(grid[0])
        # two rules: if the row begins with 0, flip row
        # this is because 1xxxx > 0xxxx in all cases
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        # if there are more 0 in a column than 1, flip column
        # we can represent this with mathematics
        for j in range(n):
            # how many 1 in the column?
            ones = sum(grid[i][j] for i in range(m))
            # number of zeroes is m - ones
            # now multiply by the value of the column
            # represented by the binary operation
            ans += max(ones, m-ones) * (1 << (n-j-1))
        return ans
