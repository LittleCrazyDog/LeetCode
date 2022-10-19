class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def find(x):
            if d[x] != x: d[x] = find(d[x])
            return d[x]
        
        def union(x, y):
            d[find(x)] = find(y)
        
        l1, l2 = len(sentence1), len(sentence2)
        if l1 != l2: return False
        
        d = {}
        for x, y in similarPairs:
            d[x], d[y] = x, y
        for x, y in zip(sentence1, sentence2):
            d[x], d[y] = x, y
        for x, y in similarPairs:
            union(x, y)
        
        for i in range(l1):
            x, y = find(sentence1[i]), find(sentence2[i])
            if x != y: return False
        
        return True