class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # this has to be a very easy question?
        # sorting is probably required
        expected = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans
