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
            sums.append(node.val + sum(node.left) + sum(node.right))
            return sums[-1]
        sums = []
        return sum(root) / 2. in sums[:-1]