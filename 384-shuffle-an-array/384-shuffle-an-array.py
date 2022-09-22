class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.g = self.gen()

    def gen(self):
        while True:
            for p in permutations(self.nums):
                yield p
    
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return next(self.g)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()