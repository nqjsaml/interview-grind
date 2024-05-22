# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # this one here we can definitely dfs
        # my question is, is there in place modification?
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            # think postorder traversal
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # skip over targeted value
            if node.left == node.right and node.val == target:
                return None
            return node
        
        return dfs(root)
