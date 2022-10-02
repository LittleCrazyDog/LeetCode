class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {u: i for i, u in enumerate(list1)}
        best, res = 1e9, []
        
        for j, v in enumerate(list2):
            i = index1.get(v, 1e9)
            if i + j < best:
                best = i + j
                res = [v]
            elif i + j == best:
                res.append(v)
        
        return res