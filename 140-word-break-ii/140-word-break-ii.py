class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # memo = {len(s): ['']}
        # def sentences(i):
        #     if i not in memo:
        #         memo[i] = [s[i:j] + (tail and ' ' + tail)
        #                   for j in range(i+1, len(s)+1)
        #                   if s[i:j] in wordDict
        #                   for tail in sentences(j)]
        #     return memo[i]
        # return sentences(0)
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res