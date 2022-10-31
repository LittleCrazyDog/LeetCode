class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l < r and arr[l+1] >= arr[l]:
            l += 1
        if l == len(arr)-1: return 0
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        toRemove = min(len(arr) - l - 1, r)
        for iL in range(l+1):
            if arr[iL] <= arr[r]:
                toRemove = min(toRemove, r-iL-1)
            elif r < len(arr)-1:
                r += 1
            else:
                break
        return toRemove