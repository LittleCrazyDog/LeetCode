# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def robsub(node):
            # returns tuple of size two (now, later)
            # now: max money earned if node is robbed
            # later, max money earned if node is not robbed
            
            # base case:
            if not node: return (0, 0)
            
            # get values:
            left, right = robsub(node.left), robsub(node.right)
            
            # rob now
            now = node.val + left[1] + right[1]
            
            # rob later
            later = max(left) + max(right)
            
            return (now, later)
        
        return max(robsub(root))