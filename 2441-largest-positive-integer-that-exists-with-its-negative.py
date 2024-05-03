class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # let's check the existence of elements in the array
        mp = {}
        ans = -1
        for i in range(len(nums)):
            # what should be the mapping?
            # probably index, value
            if nums[i] < 0 and -nums[i] in mp.values():
                ans = max(ans, -nums[i])
            elif nums[i] > 0 and -nums[i] in mp.values():
                ans = max(ans, nums[i])
            # we will always have to insert the value into the array
            mp[i] = nums[i]
        return ans
