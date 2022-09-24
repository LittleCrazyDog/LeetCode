class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = defaultdict(int)
        unpaired_count = 0
        res = 0
        for word in words:
            # ee
            if word[0] == word[1]:
                # check if we already have a 'ee' to match
                if c[word] > 0:
                    res += 4
                    c[word] -= 1
                    unpaired_count -= 1
                    pass
                else:
                    # record this 'ee'
                    c[word] += 1
                    unpaired_count += 1
                    pass
            # em
            else:
                # check if we alrady have a 'me' to match
                if c[word[::-1]] > 0:   # there is already a 'me' can match this 'em'
                    res += 4    # update the result
                    c[word[::-1]] -= 1  # this 'me' is already used, delete it from dict
                else:
                    c[word] += 1
        
        if unpaired_count > 0: res += 2
        
        return res