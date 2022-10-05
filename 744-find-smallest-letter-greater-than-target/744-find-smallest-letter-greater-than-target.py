class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low, high = 0, len(letters)-1
        while low <= high:
            mid = (low + high) // 2
            if target >= letters[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return letters[low]