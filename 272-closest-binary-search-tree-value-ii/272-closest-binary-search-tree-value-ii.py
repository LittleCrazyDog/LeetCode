# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = []
        pre_stack = []
        suc_stack = []
        
        while root:
            if root.val < target:
                pre_stack.append(root)
                root = root.right
            else:
                suc_stack.append(root)
                root = root.left
        
        def get_pre(stack):
            if stack:
                pre = stack.pop()
                p = pre.left
                while p:
                    stack.append(p)
                    p = p.right
                return pre
        
        def get_suc(stack):
            if stack:
                suc = stack.pop()
                p = suc.right
                while p:
                    stack.append(p)
                    p = p.left
                return suc
        
        pre = get_pre(pre_stack)
        suc = get_suc(suc_stack)
        
        while k:
            k -= 1
            if (pre and not suc) or (pre and suc and abs(pre.val-target) <= abs(suc.val-target)):
                res.append(pre.val)
                pre = get_pre(pre_stack)
            else:
                res.append(suc.val)
                suc = get_suc(suc_stack)
        return res