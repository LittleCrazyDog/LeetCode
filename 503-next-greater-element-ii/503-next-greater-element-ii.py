class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Loop once, we can get the next great number of a normal array
        # Loop twice, we can get the next great number of a circular array
        
        # Complexity:
        # Time: O(N) for one pass
        # Space: O(N) in worst case
        
        stack, res = [], [-1] * len(nums)
        for i in list(range(len(nums)))*2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res