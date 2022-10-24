# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        leftCount = self.countNodes(root.left)
        if k <= leftCount: return self.kthSmallest(root.left, k)
        if k == leftCount+1: return root.val
        if k > leftCount+1: return self.kthSmallest(root.right, k-1-leftCount)
        
    def countNodes(self, node):
        if not node: return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)