# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        hi = 1
        while reader.get(hi) < target:
            hi <<= 1
        lo = hi >> 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if reader.get(mid) < target:
                lo = mid + 1
            elif reader.get(mid) > target:
                hi = mid - 1
            else:
                return mid
        return -1