class Solution:
    def frequencySort(self, s: str) -> str:
        # Counter & Sorting
        # Time: O(NlogN)
        # Space: O(N)
        # cnt = Counter(s)
        # s = list(s)
        # s.sort(key = lambda x: (-cnt[x], x))
        # return ''.join(s)
        
        # Counter & Sorting Distinct Characters
        cnt = Counter(s)
        arr = [[freq, c] for c, freq in cnt.items()]
        arr.sort(key = lambda x: -x[0])
        res = []
        for freq, c in arr:
            res.append(freq*c)
        return ''.join(res)