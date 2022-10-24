# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        oldPaths = defaultdict(int)
        oldPaths[0] = 1
        self.dfs(root, targetSum, 0, oldPaths)
        return self.result
    
    def dfs(self, root, targetSum, currPathSum, oldPaths):
        if not root: return
        currPathSum += root.val
        self.result += oldPaths[currPathSum - targetSum]
        oldPaths[currPathSum] += 1
        self.dfs(root.left, targetSum, currPathSum, oldPaths)
        self.dfs(root.right, targetSum, currPathSum, oldPaths)
        oldPaths[currPathSum] -= 1