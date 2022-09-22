class Solution:

    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

#     def reset(self) -> List[int]:
        

#     def shuffle(self) -> List[int]:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()