class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        
        res = []
        while num > 1:
            for d in range(9, 1, -1):
                if num % d == 0:
                    num /= d
                    res.append(d)
                    break
            else:
                return 0
        
        res = int(''.join(map(str, res[::-1])))
        return res if res < 2**31 else 0