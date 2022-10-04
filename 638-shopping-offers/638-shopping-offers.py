class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        d = {}
        def dfs(cur):
            if tuple(cur) not in d:
                val = sum(cur[i]*price[i] for i in range(len(needs)))
                for spec in special:
                    tmp = [cur[j]-spec[j] for j in range(len(needs))]
                    if min(tmp) >= 0:   # skip deals that exceed needs
                        val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1])
                d[tuple(cur)] = val
            return d[tuple(cur)]
        return dfs(needs)