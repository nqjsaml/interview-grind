class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # question: how many mhts can a graph have at most?
        # this is either ONE or TWO, due to the fact that we want to find its center
        # base case: one node tree
        if n == 1:
            return [0]
        # we will actually have to populate a graph and adjacency list
        g = defaultdict(list)
        degree = [0] * n
        # graph population with given edges
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            degree[a] += 1
            degree[b] += 1
        # we'll have bfs here, so we need a queue but here we'll have all leaves
        q = collections.deque(i for i in range(n) if degree[i] == 1)
        ans = []
        # begin bfs
        while q:
            # think of peeling onions down to the very center
            ans.clear()
            for _ in range(len(q)):
                cur = q.popleft()
                ans.append(cur)
                # remove neighbors
                for neighbor in g[cur]:
                    degree[neighbor] -= 1
                    # and if a leaf, add to the queue
                    if degree[neighbor] == 1:
                        q.append(neighbor)
        return ans
