# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = deque()
        stack = []
        run = root
        
        while run or stack:
            if run:
                stack.append(run)
                run = run.left
            else:
                node = stack.pop()
                if len(res) < k:
                    res.append(node.val)
                elif node.val-target<target-res[0]:
                    res.popleft()
                    res.append(node.val)
                else:
                    return res
                run = node.right
        return res