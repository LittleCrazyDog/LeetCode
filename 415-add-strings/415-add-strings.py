class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        
        while len(num2) > 0 or len(num1) > 0:
            n1 = n2 = 0
            if num1: n1 = ord(num1.pop()) - ord('0')
            if num2: n2 = ord(num2.pop()) - ord('0')

            carry, remain = divmod(n1 + n2 + carry, 10)
            res.append(remain)
        
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]