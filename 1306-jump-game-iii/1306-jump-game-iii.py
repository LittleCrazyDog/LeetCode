class Solution:
    def canReach(self, arr: List[int], i: int) -> bool:
        if 0 <= i < len(arr) and arr[i] >= 0:
            arr[i] = -arr[i]
            return arr[i] == 0 or self.canReach(arr, i + arr[i]) or self.canReach(arr, i - arr[i])
        return False