class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []
        
        # build hashmap
        for ch in p:
            hm[ch] += 1
            
        # initail full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
        
        # slide the window with stride 1:
        for i in range(sL-pL+1):
            if i > 0 and s[i-1] in hm:
                hm[s[i-1]] += 1
            if s[i+pL-1] in hm:
                hm[s[i+pL-1]] -= 1
            
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()):
                res.append(i)
        
        return res