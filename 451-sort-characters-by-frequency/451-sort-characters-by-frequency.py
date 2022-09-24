class Solution:
    def frequencySort(self, s: str) -> str:
        # Counter & Sorting
        # Time: O(NlogN)
        # Space: O(N)
        cnt = Counter(s)
        s = list(s)
        s.sort(key = lambda x: (-cnt[x], x))
        return ''.join(s)