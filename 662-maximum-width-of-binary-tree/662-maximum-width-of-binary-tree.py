# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width, level = 0, [(root, 1)]
        
        while level:
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:
                    next_level.append((item.left, 2*num))
                if item.right:
                    next_level.append((item.right, 2*num+1))
            level = next_level
        
        return width