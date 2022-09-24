# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute-Force
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return
        # dfs back down
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
        
        # test back down
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)