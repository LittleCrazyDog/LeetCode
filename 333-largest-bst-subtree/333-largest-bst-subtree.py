# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class SubTree(object):
#     def __init__(self, largest, n, min, max):
#         self.largest = largest
#         self.n = n
#         self.min = min
#         self.max = max

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
        
        return dfs(root)[0]
    
#     def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
#         res = self.dfs(root)
#         return res.largest
    
#     def dfs(self, root):
#         if not root:
#             return SubTree(0, 0, float('inf'), float('-inf'))
        
#         left = self.dfs(root.left)
#         right = self.dfs(root.right)
        
#         if root.val > left.max and root.val < right.min:
#             n = left.n + right.n + 1
#         else:
#             n = float('-inf')
        
#         largest = max(left.largest, right.largest, n)
#         return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))