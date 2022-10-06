"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', val: int) -> 'Node':
        node = Node(val)
        if not head:
            node.next = node
            return node
        prev, cur = head, head.next
        while 1:
            if prev.val <= val <= cur.val:
                break
            elif prev.val > cur.val and (val < cur.val or val > prev.val):
                break
            prev, cur = prev.next, cur.next
            if prev == head:
                break
        prev.next = node
        node.next = cur
        return head