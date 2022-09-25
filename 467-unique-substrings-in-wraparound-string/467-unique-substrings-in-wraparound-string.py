class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())