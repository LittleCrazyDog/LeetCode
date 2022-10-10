class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # The smaller numbers on the right of a number are exactly those that jump from its right
        # to its left during a stable sort. So I do mergesort with added tracking of those
        # right-to-left jumps.
        
        # Sort (index, value) pairs. 
        # The value is used for sorting and the index is used for tracking the jumps
        
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller