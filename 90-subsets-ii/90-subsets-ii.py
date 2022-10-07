class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, pos = [[]], {}
        for n in nums:
            start, l = pos.get(n, 0), len(res)
            res += [res[i] + [n] for i in range(start, len(res))]
            pos[n] = l
        return res