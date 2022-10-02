class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution I - Memoization - Top Down
        m, n = len(word1), len(word2)
        @cache
        def lcs(i, j):  # find longest common subsequence
            if i == m or j == n:
                return 0
            return 1 + lcs(i+1, j+1) if word1[i] == word2[j] else max(lcs(i+1, j), lcs(i,j+1))
        # substract the lcs length from both the strings
        # the difference is the number of characters that has no deleted.
        return m + n - 2*lcs(0, 0)