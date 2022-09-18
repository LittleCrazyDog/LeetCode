class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        area = 0
        
        left, right = 0, len(height)-1
        
        left_height, right_height = height[left], height[right]
        
        while left < right:
            left_height = max(left_height, height[left])
            right_height = max(right_height, height[right])
            
            if left_height <= right_height:
                area += left_height - height[left]
                left += 1
            else:
                area += right_height - height[right]
                right -= 1
        
        return area