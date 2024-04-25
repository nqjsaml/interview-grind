class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # the ideal string, recall that the string t is a subsequence of s
        # and the difference of all two adjacent letters in t <= k
        # 2d top-down dp solution below
        """
        # notice we only need to check the last letter of the subsequence
        # created from the first i letters of s
        dp = [[-1] * 26 for _ in range(len(s))]

        # helper function to help assist with dynamic programming
        def helper(i: int, c: int, dp: List[int], s: str, k: int) -> int:
            # found the value!
            if dp[i][c] != -1:
                return dp[i][c]
            # base case: not seen yet
            dp[i][c] = 0
            # subsequence will become one letter longer if included
            match = (c == ord(s[i]) - ord('a'))
            if match:
                dp[i][c] = 1
            # recurse: may not handle current character
            if i > 0:
                dp[i][c] = helper(i-1, c, dp, s, k)
                # check all transitions to previous letters
                # and recurse through these too
                if match:
                    for p in range(26):
                        if abs(c-p) <= k:
                            dp[i][c] = max(dp[i][c], helper(i-1, p, dp, s, k)+1)
            return dp[i][c]

        ans = 0
        for c in range(26):
            ans = max(ans, helper(len(s)-1, c, dp, s, k))
        return ans
        """
        # bottom-up dp with less space; we only need to check the
        # previous dp values
        dp = [0] * 26
        ans = 0
        # begin dp
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            # best substring length so far
            temp = 0
            for p in range(26):
                if abs(p-c) <= k:
                    # this line ensures that the previous char is in s
                    temp = max(temp, dp[p])
            # append s[i] to the previous LIS
            dp[c] = max(dp[c], temp+1)
            ans = max(ans, dp[c])
        return ans
