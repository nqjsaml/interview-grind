# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # probably some sort of two pointer maintaining?
        # we could try to use some sort of monotonic stack, but
        # that requires some extra space.
        cur = head
        # reversing the list in place can use no extra space, but I will
        # opt to not do that, instead use a queue
        q = deque()
        # we'll iterate through the front of the LL
        while cur:
            # maintains the maximum value seen so far
            while q and q[-1].val < cur.val:
                q.pop()
            # attaches the current part of the LL to the end of the queue
            if q:
                q[-1].next = cur
            q.append(cur)
            cur = cur.next
        return q[0]
