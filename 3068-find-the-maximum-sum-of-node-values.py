class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # lol what? the idea is one can xor any two
        # nodes as all of them are connected
        # hence, edges is irrelevant.
        total = sum(nums)
        # we always want to find if we add anything
        total_diff = 0
        pos_count = 0
        min_abs_diff = inf

        for num in nums:
            diff = (num ^ k) - num
            if diff > 0:
                total_diff += diff
                pos_count += 1
            min_abs_diff = min(min_abs_diff, abs(diff))

        # need the xors count to be even
        if pos_count % 2 == 1:
            total_diff -= min_abs_diff
        return total + total_diff
