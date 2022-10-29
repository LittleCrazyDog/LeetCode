# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        curr = head
        numNodes = len(nodes)
        for _ in range(k % numNodes):
            nodes[len(nodes)-2].next = None
            newHead = nodes.pop()
            newHead.next = curr
            curr = newHead
        return curr