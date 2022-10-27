class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        LA = [i // N * 100 + i % N for i in range(N*N) if img1[i // N][i % N]]
        LB = [i // N * 100 + i % N for i in range(N*N) if img2[i // N][i % N]]
        c = Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])