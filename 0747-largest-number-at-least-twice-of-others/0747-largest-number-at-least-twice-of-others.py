class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest = -1
        secondHighest = -1
        highestIndex = -1
        for i, n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n
        if highest < secondHighest * 2: return -1
        return highestIndex