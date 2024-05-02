class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # think of this as shortest path? so the only way to go is some sort of bfs
        deadset = set(deadends)
        # base case and easiest-return cases: can't turn lock or lock starts at correct combo
        if '0000' in deadset:
            return -1
        if target == '0000':
            return 0
        # we'll have the beginning queue start with '0000' and the initial moves
        q = collections.deque([('0000', 0)])
        visited = set()
        visited.add('0000')
        # begin bfs
        while q:
            cur, ans = q.popleft()
            # terminating case
            if cur == target:
                return ans
            # adjust the combination of the lock, digit by digit, up and down
            # if we haven't seen them before and they don't produce a deadend, continue
            for i in range(4):
                # add or subtract? mod accounts for edge cases
                for s in [-1, 1]:
                    nd = (int(cur[i])+s) % 10
                    nc = cur[:i] + str(nd) + cur[i+1:]
                    if nc not in visited and nc not in deadset:
                        visited.add(nc)
                        q.append((nc, ans+1))
        # if we get here, not possible to adjust the lock further
        return -1
