class NumArray:
    # Binary Indexed Tree Approach

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT = [0] * (self.n+1)
        
        for i, v in enumerate(nums):
            self.updateBIT(i, v)
    
    def getsumBIT(self, index):
        index += 1
        res = 0
        
        while index > 0:
            res += self.BIT[index]
            index -= index & -index
        
        return res
    
    def updateBIT(self, index, delta):
        index += 1
        while index <= self.n:
            self.BIT[index] += delta
            index += index & -index
    
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.updateBIT(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.getsumBIT(right) - self.getsumBIT(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)