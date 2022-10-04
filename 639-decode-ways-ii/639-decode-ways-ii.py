class Solution:
    def numDecodings(self, s: str) -> int:
        # e0 = current number of ways we could decode, ending on any number
        # e1 = current number of ways we could decode, ending on an open 1
        # e2 = current number of ways we could decode, ending on an open 2
        
        # if c == '*', then the number of ways to finish in total is:
        # we could put * as a single digit number (9*e0), or
        # we could pair * as a 2 digit number 1* in 9*e1 ways, or
        # we could pair * as a 2 digit number 2* in 6*e2 ways
        
        # if c != '*', then the number of ways to finish in total is:
        # we could put c as a single digit if it is not zero((c>'0')*e0), or
        # we could pair c with our open 1, or
        # we could pair c with our open 2 if it is 6 or less ((c<='6')*e2)
        
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0