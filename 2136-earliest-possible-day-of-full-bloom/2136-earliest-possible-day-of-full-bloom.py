class Solution:
    def earliestFullBloom(self, P: List[int], G: List[int]) -> int:
        pairs = sorted((g, p) for g, p in zip(G, P))
        P = [p for _, p in pairs]
        G = [g for g, _ in pairs]
        ans, Q = sum(P), sum(P)
        p_acc = [0] + list(accumulate(P))
        for i in range(len(pairs)):
            ans = max(ans, Q - p_acc[i] + G[i])
        return ans