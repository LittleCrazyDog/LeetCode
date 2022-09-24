class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = defaultdict(int)
        res = 0
        unpaired_word = 0
        
        for word in words:
            c[word] += 1
        
        for w in list(c.keys()):
            # ee
            if w[0] == w[1]:
                res += 4 *(c[w]//2)
                c[w] = c[w] % 2
                if c[w] > 0:
                    unpaired_word += 1
            # em
            else:
                res += 4 * min(c[w], c[w[::-1]])
                del c[w]
                del c[w[::-1]]
                
        if unpaired_word > 0: res += 2
        
        return res