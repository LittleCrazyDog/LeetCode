class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Basic Idea
        # First char of input string is first char of repeated substring
        # Last char of input string is last char of repeated substring
        # Let S1 = S + S (where S in input string)
        # Remove 1 and last char of S1. Let it be S2
        # If S exists in S2 then return true else false
        # Let i be index in S2 where S starts then repeated substring length i+1 and repeated substring S[0:i+1]
        
        ss = (s+s)[1:-1]
        return ss.find(s) != -1