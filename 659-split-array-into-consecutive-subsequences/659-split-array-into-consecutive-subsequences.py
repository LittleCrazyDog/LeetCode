class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Greedy Algorithm
        # left is a hashmap, left[i] counts the number of i that I haven't placed yet
        # end is a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
        # Then I tried to split the nums one by one
        # If I could either add a number to the end of a existing consecutive subsequence nor find two following
        # numbers in the left, I returned False
        
        left = Counter(nums)
        end = Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i-1] > 0:
                end[i-1] -= 1
                end[i] += 1
            elif left[i+1] and left[i+2]:
                left[i+1] -= 1
                left[i+2] -= 1
                end[i+2] += 1
            else:
                return False
        return True