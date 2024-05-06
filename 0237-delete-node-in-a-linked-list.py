# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # basically here do we need to navigate to
        # the node and remove its previous pointer?
        # nah, just change the order
        node.val = node.next.val
        node.next = node.next.next
