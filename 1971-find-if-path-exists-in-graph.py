class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # literally this would just be bfs wouldn't it
        # but first let's construct the actual graph and adjacency list
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        # this is doable with dfs, or bfs, or union find (solutions there follow below)
        # but here will be the bfs solution
        q = collections.deque([source])
        visited = set([source])
        # begin bfs
        while q:
            cur = q.popleft()
            # return case
            if cur == destination:
                return True
            # add all neighbors to the queue
            for neighbor in g[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        # if we get here, then no such path exists
        return False
