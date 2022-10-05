# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        curr = head
        while curr:
            if curr in hashSet:
                return curr
            hashSet.add(curr)
            curr = curr.next
        return None