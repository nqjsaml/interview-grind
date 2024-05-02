class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # another hard problem????
        # populate a graph and count array
        ans = [0] * n
        # this represents the number of nodes in the subtree rooted
        # at this node
        counts = [1] * n
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        # first dfs: update counts and result
        # by calculating the distance from root to all other nodes
        def dfs1(node: int, parent: int) -> None:
            for child in g[node]:
                if child != parent:
                    dfs1(child, node)
                    counts[node] += counts[child]
                    ans[node] += ans[child] + counts[child]

        # second dfs: calculates distances from all other nodes
        def dfs2(node: int, parent: int) -> None:
            for child in g[node]:
                if child != parent:
                    ans[child] = ans[node] - 2*counts[child] + n
                    dfs2(child, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
