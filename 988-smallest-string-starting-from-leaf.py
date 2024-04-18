# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # is this not basically dfs because we need to check the whole thing
        # let's just do it!
        def dfs(node: Optional[TreeNode], ans: str) -> str:
            # base case
            if not node:
                return ''
            # append the current value to the string as represented by lexicographical order
            ans = chr(node.val+ord('a')) + ans
            # leaf node which is where we want to return from: no children
            if not node.left and not node.right:
                return ans
            # obtain left paths and right paths, returning the smallest one if required
            # Python can automatically compare strings so this is totally fine to do
            # recurse
            lp = dfs(node.left, ans)
            rp = dfs(node.right, ans)
            if lp and rp:
                return min(lp, rp)
            elif lp:
                return lp
            else:
                return rp
        return dfs(root, '')
