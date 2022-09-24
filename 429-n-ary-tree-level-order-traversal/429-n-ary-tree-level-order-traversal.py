"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None: return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                for child in curr.children:
                    q.append(child)
            ans.append(level)
        return ans