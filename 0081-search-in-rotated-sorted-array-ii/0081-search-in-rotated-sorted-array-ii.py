class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return True
            while lo < mid and nums[lo] == nums[mid]: lo += 1
            # the first half is ordered
            if nums[lo] <= nums[mid]:
                # if target is in the first half
                if nums[lo] <= target < nums[mid]: hi = mid - 1
                else: lo = mid + 1
            # the second half is ordered
            else:
                # if target is in the second half
                if nums[mid] < target <= nums[hi]: lo = mid + 1
                else: hi = mid - 1
        return False