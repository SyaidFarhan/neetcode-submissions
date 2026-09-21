# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dumy = ListNode(0, head)
        leftprev, cur = dumy, head
        for i in range(left-1) :
            leftprev, cur = cur, cur.next

        prev = None
        for i in range (right - left + 1) :
            tmpnext = cur.next
            cur.next = prev
            prev, cur = cur, tmpnext
        leftprev.next.next = cur
        leftprev.next = prev
        return dumy.next
