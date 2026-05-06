# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head

        while f:
            s = s.next
            if not f.next:
                return False
            f = f.next.next
            if s == f:
                return True

        return False