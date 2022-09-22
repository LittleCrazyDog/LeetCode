# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root):
            if not root:
                return -1
            height = max(dfs(root.left), dfs(root.right)) + 1
            if height >= len(res):
                res.append([])
            res[height].append(root.val)
            return height
        dfs(root)
        return res