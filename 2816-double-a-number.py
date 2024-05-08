# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # double it! probably very similar to #2
        # a possibility is to reverse, multiply, then reverse again
        # to make it basically #2
        # no, this is going to require DLL and two pointers lol!
        cur, prev = head, None
        while cur:
            # perform the multiplication as specified
            num = cur.val * 2
            if num < 10:
                cur.val = num
            # number is greater than 10 and not first node in LL
            # note: since multiplying by 2 only, carry can only be 0 or 1
            elif prev:
                # current digit becomes the unit digit
                # and carry gets added to previous digit
                cur.val = num % 10
                prev.val += 1
            # this is the first node so need to create a new node
            # with the current LL as its next pointer
            else:
                head = ListNode(1, cur)
                cur.val = num % 10
            prev = cur
            cur = cur.next
        return head
