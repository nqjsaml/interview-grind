class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # more backtracking yay!
        ans = []

        def backtrack(start: int, cur: List[int]) -> None:
            # always adds the current set
            ans.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur)
                # this part here does the backtracking
                cur.pop()

        # observe: there must be a total of 2^n subsets
        # because we can choose each nums[i] as part of the subset
        # or not
        backtrack(0, [])
        return ans
