class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pC = Counter(p)
        res = []
        window = None
        for i in range(len(s)-len(p)+1):
            if i == 0:
                window = Counter(s[i:i+len(p)])
            else:
                minus = {s[i-1]:1}
                plus = {s[i+len(p)-1]:1}
                window -= minus
                window += plus
            if pC == window: res.append(i)
        return res