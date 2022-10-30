class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(m):
            i = j = 0
            remove = set(removable[:m+1])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(p)
        
        l, r = 0, len(removable) + 1
        while l < r:
            m = (l + r) // 2
            if check(m): l = m + 1
            else: r = m
        return l if l < len(removable) else l - 1