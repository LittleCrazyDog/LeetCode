# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, d: int) -> Optional[TreeNode]:
        if not root or d <= 0: return None
        if d == 1:
            return TreeNode(val, root, None)
        if d == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, d-1)
            root.right = self.addOneRow(root.right, val, d-1)
        return root