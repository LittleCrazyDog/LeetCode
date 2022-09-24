# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        carry, head = 0, None
        while st1 or st2 or carry:
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, remainder = divmod(d1 + d2 + carry, 10)
            head = ListNode(remainder, head)
        return head