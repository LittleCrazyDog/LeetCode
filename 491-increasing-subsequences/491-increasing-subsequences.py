class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsets(nums, 0, [], res)
        return res
    
    def subsets(self, nums, index, temp, res):
        if len(nums) >= index and len(temp) >= 2:
            res.append(temp[:])
        used = {}
        for i in range(index, len(nums)):
            if len(temp) > 0 and temp[-1] > nums[i]: continue
            if nums[i] in used: continue
            used[nums[i]] = True
            temp.append(nums[i])
            self.subsets(nums, i+1, temp, res)
            temp.pop()