class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Let us keep evaluate min_list, where min_list[i] = min(nums[0], ..., nums[i]).
        # Also let us traverse our nums from the end and keep stack with decreasing elements, which are more than min_list[j] for given j.
        # We will try to find 132 pattern, where nums[j] is middle number in this pattern
        
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False