class Solution:

    def __init__(self, nums: List[int]):
        self.lookup = {}
        for i, num in enumerate(nums):
            if num not in self.lookup:
                self.lookup[num] = [i]
            else:
                self.lookup[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.lookup[target]
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)