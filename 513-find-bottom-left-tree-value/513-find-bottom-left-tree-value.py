# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = 0
        while queue:
            res = queue[0].val
            queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
        
        return res