class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        a = self.below(high)
        b = self.below(low, include=False)
        return a-b if a>b else 0
    
    def below(self, n, include=True):
        res = 0
        for i in range(1, len(n)):
            res += self.number(i)
        l = self.strobogrammatic(len(n))
        if include:
            l = [num for num in l if (len(num)==1 or num[0]!='0') and num<=n]
        else:
            l = [num for num in l if (len(num)==1 or num[0]!='0') and num<n]
        return res + len(l)
    
    def strobogrammatic(self, l):
        res = []
        if l == 1:
            return ['0', '1', '8']
        if l == 2:
            return ['00', '11', '69', '96', '88']
        for s in self.strobogrammatic(l-2):
            res.append('0'+s+'0')
            res.append('1'+s+'1')
            res.append('6'+s+'9')
            res.append('8'+s+'8')
            res.append('9'+s+'6')
        return res
    
    def number(self, l):
        if l == 0: return 0
        if l % 2 == 0: return 4*(5**(l//2-1))
        if l == 1: return 3
        return 3*(5**(l//2-1))*4