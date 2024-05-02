# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # is this just dfs lol
        def dfs(node: Optional[TreeNode], total: int) -> int:
            # base case for the recursion
            if not node:
                return 0
            # each node is a digit so multiply by 10 and add correct value
            total *= 10
            total += node.val
            # no children on either side, so finished calculating sum
            if not node.left and not node.right:
                return total
            # recurse on both sides and add them
            return dfs(node.left, total) + dfs(node.right, total)
        return dfs(root, 0)
