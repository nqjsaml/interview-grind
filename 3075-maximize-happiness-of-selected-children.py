class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # greedy time!! or just sort lol.
        happiness.sort(reverse=True)
        ans = 0
        # only need to select k children
        for i in range(k):
            # because each time child is not selected, decrease happiness
            ans += max(0, happiness[i]-i)
        return ans
