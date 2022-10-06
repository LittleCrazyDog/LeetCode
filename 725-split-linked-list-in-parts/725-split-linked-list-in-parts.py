# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1. Count the length of the linked list
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
        
        # 2. Determine the length of nodes in each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k-longer_chunks)
        
        # 3. Splitting the linked list up
        prev, curr = None, head
        for idx, num in enumerate(res):
            if prev:
                prev.next = None
            res[idx] = curr
            for _ in range(num):
                prev, curr = curr, curr.next
        return res