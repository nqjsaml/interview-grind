# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # goal here is to basically check if there is no child node AND is on the left side
        # we'll do so with a simple recursion
        ans = 0
        # base case
        if not root:
            return 0
        # left child exists and leaf node (no children)
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        # recurse on both sides
        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans
