class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k, num[i] = divmod(num[i]+k, 10)
        return [int(i) for i in str(k)] + num if k else num