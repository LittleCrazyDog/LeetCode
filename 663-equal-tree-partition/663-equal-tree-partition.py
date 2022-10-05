# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def sum(node):
            if not node: return 0
            s = node.val + sum(node.left) + sum(node.right)
            if node is not root:
                cuts.add(s)
            return s
        cuts = set()
        return sum(root) / 2. in cuts