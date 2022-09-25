class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0: return list(range(len(security)))
        lft, rgt, n = [1], [1], len(security)
        
        # Build non-increasing on the left side (inclusive).
        curr = 1
        for i in range(1, n):
            if security[i] <= security[i-1]: curr += 1
            else: curr = 1
            lft.append(curr)
        
        # Build non-decreasing on the right side (inclusive).
        curr = 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]: curr += 1
            else: curr = 1
            rgt.append(curr)
        rgt.reverse()
        
        return [i for i in range(n) if lft[i] >= time + 1 and rgt[i] >= time + 1]