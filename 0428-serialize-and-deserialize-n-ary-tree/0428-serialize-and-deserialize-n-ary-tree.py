"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []
        def preorder(node):
            if not node: return
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append('#')
        preorder(root)
        return ' '.join(serial)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])
        def helper(node):
            if not tokens: return
            while tokens[0] != '#': # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)
            tokens.popleft()    # discard the '#'
        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))