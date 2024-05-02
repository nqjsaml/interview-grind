class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # is this brute forceable?
        # ig it'd be similar to #752; notice that ring[0] is the start
        # or is it similar to #1289?
        # yes, we will have to do dp here!
        dp = [[float('inf')] * len(ring) for _ in range(len(key))]
        # and also keep track of ring character positions and their index
        mp = defaultdict(list)
        for i, c in enumerate(ring):
            mp[c].append(i)
        # populate first character, accounting for ccw rotation
        for j in mp[key[0]]:
            dp[0][j] = min(j, len(ring)-j) + 1
        # now populate the remaining characters
        for i in range(1, len(key)):
            for j in mp[key[i]]:
                for k in mp[key[i-1]]:
                    # minimum over direct step count
                    # and wrap-around step count
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i-1][k] + min(abs(j-k), len(ring)-abs(j-k))+1
                    )
        # bottom row now has the minimum possible rotations
        # so just return the smallest one there
        return min(dp[-1][j] for j in mp[key[-1]])
