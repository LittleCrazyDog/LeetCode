class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def find(x):
            d.setdefault(x, x)
            if d[x] != x: d[x] = find(d[x])
            return d[x]
        def union(x, y):
            d[find(x)] = find(y)
        d = {}
        for x, y in synonyms:
            union(x, y)
        
        hs = defaultdict(set)
        for x, y in synonyms:
            rx = find(x)
            hs[rx] |= set([x, y])
        
        res = []
        for t in text.split():
            if t not in d:
                res.append([t])
            else:
                rt = find(t)
                res.append(list(hs[rt]))
        fin_res = [' '.join(sentence) for sentence in product(*res)]
        return sorted(fin_res)