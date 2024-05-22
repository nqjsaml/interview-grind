class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # recursion problem but is there an easier way?
        # we will probably have to evaluate every subset
        # time to recurse!!!
        def backtrack(start: int, cur: int) -> int:
            # termination
            if start == len(nums):
                return cur
            # sum if we xor this element and if we don't
            return backtrack(start+1, cur^nums[start]) + backtrack(start+1, cur)
        
        # start at zero because 0^anything is the thing
        return backtrack(0, 0)
