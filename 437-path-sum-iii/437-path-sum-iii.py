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
        # exit condition
        if root == None:
            return
        
        currPathSum += root.val
        oldPathWanted = currPathSum - targetSum
        
        self.result += oldPaths[oldPathWanted]
        oldPaths[currPathSum] = oldPaths[currPathSum] + 1
        
        # dfs children
        self.dfs(root.left, targetSum, currPathSum, oldPaths)
        self.dfs(root.right, targetSum, currPathSum, oldPaths)
        
        oldPaths[currPathSum] -= 1