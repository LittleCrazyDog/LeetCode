class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Bucket sort
        # 1. Distribute numbers to buckets.
        # 2. Find minimum and maximum in each buckets
        # 3. Iterate through buckets and check every difference between smallest element in one bucket
        #    and biggest in previous. Note, that here we also will check differences between say 1-st
        #    and 3-rd buckets if we have empty 2-nd bucket
        
        # lo, hi, n = min(nums), max(nums), len(nums)
        # if n <= 2 or hi == lo: return hi - lo
        # B = defaultdict(list)
        # for num in nums:
        #     ind = n-2 if num == hi else (num-lo)*(n-1)//(hi-lo)
        #     B[ind].append(num)
        # cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        # return max(y[0]-x[1] for x, y in zip(cands, cands[1:]))
        max_num = 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > max_num:
                max_num = nums[i+1] - nums[i]
        return max_num