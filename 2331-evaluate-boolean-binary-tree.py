# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # so I'm thinking just dfs through the tree
        # {0: False, 1: True, 2: OR, 3: AND}
        def dfs(node: Optional[TreeNode]) -> bool:
            # base case: child node
            if node.val == 0 or node.val == 1:
                return node.val == 1
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)
            return False
            
        return dfs(root)
