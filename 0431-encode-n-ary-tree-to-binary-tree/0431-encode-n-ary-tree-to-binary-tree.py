"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root: return None
        binary = TreeNode(root.val)
        if not root.children: return binary
        binary.left = self.encode(root.children[0])
        node = binary.left
        for child in root.children[1:]:
            node.right = self.encode(child)
            node = node.right
        return binary
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data: return None
        nary = Node(data.val, [])
        node = data.left
        while node:
            nary.children.append(self.decode(node))
            node = node.right
        return nary

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))