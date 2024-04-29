class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # finally a medium for once
        # let's first xor the whole array
        bin_nums = 0
        for num in nums:
            bin_nums ^= num
        # base case: xor-ing array equals k
        if bin_nums == k:
            return 0
        # due to properties of xor, we can xor this number with k
        ans = 0
        while k or bin_nums:
            # mod each number by 2, if the bits don't match then increment
            if k % 2 != bin_nums % 2:
                ans += 1
            k //= 2
            bin_nums //= 2
        return ans
