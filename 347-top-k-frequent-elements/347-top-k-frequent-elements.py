class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        frq = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1
        
        for z,v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []
        
        for x in range(len(nums), 0, -1):
            if x in frq:
                for i in frq[x]:
                    arr.append(i)
        
        return [arr[x] for x in range(0, k)]