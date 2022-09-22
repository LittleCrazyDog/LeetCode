# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            head.next, head, tail = tail, head.next, head
        carry = 1
        while tail:
            carry, tail.val = divmod(carry+tail.val, 10)
            if carry and not tail.next:
                tail.next = ListNode(0)
            tail.next, tail, head = head, tail.next, tail
        return head