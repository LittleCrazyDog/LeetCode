class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter(nums)
        for i in counter:
            if k > 0 and i + k in counter or k == 0 and counter[i] > 1:
                res += 1
        return res