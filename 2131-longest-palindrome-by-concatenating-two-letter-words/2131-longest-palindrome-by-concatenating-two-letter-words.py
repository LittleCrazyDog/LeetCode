class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = defaultdict(int)
        unpaired = res = 0
        for w in words:
            if w[0] == w[1]:
                if m[w] > 0:
                    m[w] -= 1
                    unpaired -= 1
                    res += 4
                else:
                    m[w] += 1
                    unpaired += 1
            else:
                if m[w[::-1]] > 0:
                    m[w[::-1]] -= 1
                    res += 4
                else:
                    m[w] += 1
        if unpaired > 0: res += 2
        return res