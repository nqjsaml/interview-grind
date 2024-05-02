# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # two ways of doing this: recursively (dfs) and iteratively (bfs)
        # for the recursive case, base case: depth of tree is one
        if depth == 1:
            # create a new tree node with value val as the new root and move the original tree
            # as its left subtree
            return TreeNode(val, left=root)
        # else commence dfs
        self.dfs(root, val, depth, 1)
        '''
        I'll implement the bfs solution here without running it
        q = collections.deque(root)
        level = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if level == depth-1:
                    left_node = TreeNode(val, cur.left)
                    cur.left = left_node
                    right_node = TreeNode(val, cur.right)
                    cur.right = right_node
                else:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            level += 1
        '''
        return root

    def dfs(self, node: Optional[TreeNode], val: int, depth: int, level: int) -> None:
        # for each non-null node cur at depth-1, create two nodes here with specified value
        if depth-1 == level:
            left_tree = TreeNode(val, left=node.left)
            right_tree = TreeNode(val, right=node.right)
            # and make these the new subtrees
            node.left = left_tree
            node.right = right_tree
            return
        # more to iterate through so continue
        if node.left:
            self.dfs(node.left, val, depth, level+1)
        if node.right:
            self.dfs(node.right, val, depth, level+1)
