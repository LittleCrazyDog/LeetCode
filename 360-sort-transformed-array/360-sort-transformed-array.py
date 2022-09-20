class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [x*x*a + x*b + c for x in nums]
        ret = [0] * len(nums)
        p1, p2 = 0, len(nums)-1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                ret[i] = nums[p1]
                p1 += 1
            else:
                ret[i] = nums[p2]
                p2 -= 1
            i += d
        return ret