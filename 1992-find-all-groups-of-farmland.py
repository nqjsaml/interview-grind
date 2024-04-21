class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # actually, we don't need bfs for this 
        # thanks @KhadimHussainDev
        ans = []
        m, n = len(land), len(land[0])
        # this is gonna be some sort of two pointer technique
        for i in range(m):
            for j in range(n):
                # we only care if farmland
                if land[i][j] == 1:
                    # this checks if this piece of land is part of another group
                    # that is above or to the left
                    if (i > 0 and land[i-1][j] == 1) or (j > 0 and land[i][j-1] == 1):
                        continue
                    # here it is not so, so record current coordinate with the top-left coordinate filled in
                    cur = [i, j]
                    x, y = i, j
                    # find the bottom-right coordinate by incrementing (x, y) until hitting a 0
                    while x < m and land[x][j] == 1:
                        x += 1
                    while y < n and land[i][y] == 1:
                        y += 1
                    # need to subtract one here
                    cur.append(x-1)
                    cur.append(y-1)
                    ans.append(cur)
        return ans
