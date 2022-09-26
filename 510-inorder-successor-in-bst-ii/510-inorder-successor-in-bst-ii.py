"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left: node = node.left
            return node
        
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        
        return None