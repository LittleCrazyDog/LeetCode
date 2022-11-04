class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] means the minimum number of ops required to convert word1[:i] to word2[:j]
        
        #   if word1[i-1] == word2[j-1]:
        #       dp[i][j] = dp[i-1][j-1]
        #   else:
        #       dp[i][j] = 1 + min('insert', 'remove', 'replace')
        #           'replace':  From dp[i-1][j-1], replace word1[i-1] with word2[j-1], to dp[i][j]

        #           'remove':   From dp[i][j], remove word1[i-1], to dp[i-1][j]
        #           dp[i-1][j]: word1[:i-1] ----ops---> word2[:j] (Already Know)
        #           dp[i][j]:   word1[:i] ---1 remove--> word1[:i-1] ----ops---> word2[:j]

        #           'insert':   From dp[i][j-1],
        #           dp[i][j-1]: word1[:i] ----ops---> word2[:j-1] (Already Know)
        #           dp[i][j]:   word1[:i] ----ops---> word2[:j-1] ---1 insert--> word2[:j]

        #       dp[i][j] = 1 + min('insert', 'remove', 'replace')
        #       dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # setup
        for i in range(m + 1):
            # i times remove
            dp[i][0] = i
        
        for j in range(n + 1):
            # j times insert
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        return dp[-1][-1]