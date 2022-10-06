class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        while idx < len(bits):
            if idx == len(bits)-1: return True
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1
        return False