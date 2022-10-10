class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
                for word in dictionary if len(word) == n}
        if not diffs:
            return str(n)
        bits = max((i for i in range(2**n) if all(d & i for d in diffs)),
                   key = lambda x: sum((x>>i)&3==0 for i in range(n-1))) + 2**n
        res, lo = [], 0
        for hi in range(n+1):
            if (bits>>hi) & 1:
                res += [str(hi-lo)] if hi > lo else []
                res += [target[hi]] if hi < n else []
                lo = hi + 1
        return ''.join(res)