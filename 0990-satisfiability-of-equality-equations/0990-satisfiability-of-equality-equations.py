class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        
        uf = {x: x for x in 'abcdefghijklmnopqrstuvwxyz'}
        for x, e, _, y in equations:
            if e == '=':
                uf[find(x)] = find(y)
        
        return not any(e == '!' and find(x) == find(y) for x, e, _, y in equations)