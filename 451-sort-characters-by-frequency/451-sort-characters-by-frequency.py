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
        # Time: O(N+KlogK)
        # Space: O(N)
        # cnt = Counter(s)
        # arr = [[freq, c] for c, freq in cnt.items()]
        # arr.sort(key = lambda x: -x[0])
        # res = []
        # for freq, c in arr:
        #     res.append(freq*c)
        # return ''.join(res)
        
        # Counter & Bucket Sort
        # Time: O(N)
        # Space: O(N)
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)
        
        res = []
        for freq in range(n, -1, -1):
            for c in bucket[freq]:
                res.append(c * freq)
        return ''.join(res)