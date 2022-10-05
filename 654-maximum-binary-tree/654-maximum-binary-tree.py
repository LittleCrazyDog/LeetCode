# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # We keep track of a stack, and make sure the numbers in stack is decreasing order.
        # For each new num, we make it into a TreeNode first.
        # Then:
        # 0. If stack is empty, we push the node into stack and continue
        # 1. If new value is smaller than the node value on top of the stack, 
        #    we append TreeNode as the right node of top of stack.
        # 2. If new value is larger, we keep going from the stack until the stack is EMPTY OR top of stack node value
        #    is greater than the new value. We append the last poped node as left node of the new node.
        stack = []
        for x in nums:
            n = TreeNode(x)
            while stack and x > stack[-1].val:
                n.left = stack.pop()
            if stack:
                stack[-1].right = n
            stack.append(n)
        return stack[0]