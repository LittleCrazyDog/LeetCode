class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Total hamming distance for the i-th bit = 
        # (the number of zeros in the i-th position) *
        # (the number of ones in the i-th position).
        
        bits = [[0, 0] for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i][num % 2] += 1
                num //= 2
        return sum(x * y for x, y in bits)