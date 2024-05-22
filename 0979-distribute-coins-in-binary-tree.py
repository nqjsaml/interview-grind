# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # now I wonder, should we maintain a previous pointer
        # with the value of the top node.val?
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            # base case, postorder traversal
            if not node:
                return 0
            # recurse
            lt = dfs(node.left)
            rt = dfs(node.right)
            # positive if giving to parents
            # negative if taking from them
            ans += (abs(lt) + abs(rt))
            # what should the leaf return to its parent?
            # the value of coins it has PLUS
            # the value of both its left and right trees
            # minus one
            return lt + rt + node.val - 1

        dfs(root)
        return ans
