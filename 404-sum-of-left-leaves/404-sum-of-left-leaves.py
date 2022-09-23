# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive DFS
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     def dfs(root, isLeft):
    #         if not root: return 0
    #         if not root.left and not root.right:
    #             return root.val if isLeft else 0
    #         return dfs(root.left, True) + dfs(root.right, False)
    #     return dfs(root, False)
    
    # Iterative DFS
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     s, ans = deque([(root, False)]), 0
    #     while s:
    #         cur, isLeft = s.pop()
    #         if not cur.left and not cur.right and isLeft:
    #             ans += cur.val
    #         if cur.right:
    #             s.append((cur.right, False))
    #         if cur.left:
    #             s.append((cur.left, True))
    #     return ans
    
    # BFS
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, False)]), 0
        while q:
            cur, isLeft = q.popleft()
            if not cur.left and not cur.right and isLeft:
                ans += cur.val
            if cur.right:
                q.append((cur.right, False))
            if cur.left:
                q.append((cur.left, True))
        return ans