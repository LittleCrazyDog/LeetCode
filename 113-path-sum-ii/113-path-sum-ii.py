# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    
    def dfs(self, root, targetSum, path, res):
        if not root: return
        
        if not root.left and not root.right and root.val == targetSum:
            path.append(root.val)
            res.append(path)
        
        self.dfs(root.left, targetSum-root.val, path+[root.val], res)
        self.dfs(root.right, targetSum-root.val, path+[root.val], res)