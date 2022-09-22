# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # With pure reverse helper
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(head):
            rev = None
            while head:
                head.next, head, rev = rev, head.next, head
            return rev
        head = node = reverse(head)
        while node.val == 9:
            node.val = 0
            if not node.next:
                node.next = ListNode(0)
            node = node.next
        node.val += 1
        return reverse(head)