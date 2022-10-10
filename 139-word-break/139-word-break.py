class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]