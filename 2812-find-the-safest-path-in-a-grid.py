# for this question, we'll also need to implement union-find
# so I will comment it thoroughly
"""
recall that union find is meant to find representatives of
disjoint sets via two operations, union and find
"""
class UnionFind:
    # think of these as two trees, so we need a parents' array
    # and a size array, these are both sets of n items
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    # this finds a particular item in one set
    # this requires the element x to be its own parent
    def find(self, x: int) -> int:
        # so if it isn't, then recursively move x back
        # directly underneath its own representative
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # this finds the union of two sets, a and b
    def union(self, a: int, b: int) -> bool:
        # finds the required elements
        pa, pb = self.find(a), self.find(b)
        # elements are in the same set
        if pa == pb:
            return False
        # in both of these situations, move the smaller-
        # ranked item underneath the larger-ranked one
        # and adjust their ranks accordingly
        if self.size[pa] > self.size[pb]:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # this is definitely some sort of bfs question
        # we also need Dijkstra's algorithm here, hard question
        # and we will need union-find as discussed above
        n = len(grid)
        # easiest case: beginning or end has thief
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        # set up bfs and a distance array for each thief
        q = deque()
        dist = [[-1] * n for _ in range(n)]
        # find the distance to each thief from start
        # their locations will also be put into the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0
        # efficient directions tuple, and initiate bfs
        # now update the Manhattan distance of every cell in
        # relation to thieves
        # the goal here is the shortest distance to every thief
        dirs = (-1, 0, 1, 0, -1)
        while q:
            x, y = q.popleft()
            for dx, dy in pairwise(dirs):
                xp, yp = x + dx, y + dy
                if 0 <= xp < n and 0 <= yp < n and dist[xp][yp] == -1:
                    dist[xp][yp] = dist[x][y] + 1
                    q.append((xp, yp))
        # now do union-find and binary-search
        # need to sort queue first in reverse
        q = ((dist[i][j], i, j) for i in range(n) for j in range(n))
        q = sorted(q, reverse=True)
        uf = UnionFind(n * n)
        # go through the queue now and add to the union-find set
        for d, x, y in q:
            for dx, dy in pairwise(dirs):
                xp, yp = x + dx, y + dy
                if 0 <= xp < n and 0 <= yp < n and dist[xp][yp] >= d:
                    uf.union(x * n + y, xp * n + yp)
            # start and end points are in the same component, so return
            # the current distance
            if uf.find(0) == uf.find(n * n - 1):
                return int(d)
        return 0
