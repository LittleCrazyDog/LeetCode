class NumArray:
    # Segment Tree Approach

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg_tree = [dict() for _ in range(4*self.n)]
        
        def build(i, j, idx):
            self.seg_tree[idx]['left'] = i
            self.seg_tree[idx]['right'] = j
            
            if i == j:
                self.seg_tree[idx]['val'] = nums[i]
                return
            
            mid = (i+j)//2
            
            build(i, mid, 2*idx)
            build(mid+1, j, 2*idx+1)
            
            self.seg_tree[idx]['val'] = self.seg_tree[2*idx]['val'] + self.seg_tree[2*idx+1]['val']
        
        build(0, self.n-1, 1)   # start the tree from 1

    def update(self, index: int, val: int) -> None:
        
        def seg_update(index, val, idx):
            i = self.seg_tree[idx]['left']
            j = self.seg_tree[idx]['right']
            
            if i == j and i == index:
                self.seg_tree[idx]['val'] = val
                return
            
            mid = (i+j)//2
            
            if index <= mid:
                seg_update(index, val, 2*idx)
                self.seg_tree[idx]['val'] = self.seg_tree[2*idx]['val'] + self.seg_tree[2*idx+1]['val']
            else:
                seg_update(index, val, 2*idx+1)
                self.seg_tree[idx]['val'] = self.seg_tree[2*idx]['val'] + self.seg_tree[2*idx+1]['val']
        
        seg_update(index, val, 1)

    def sumRange(self, left: int, right: int) -> int:
        
        def query(left, right, idx):
            i = self.seg_tree[idx]['left']
            j = self.seg_tree[idx]['right']
            
            if i == left and j == right:
                return self.seg_tree[idx]['val']
            
            mid = (i+j)//2
            
            if i <= left and right <= mid:
                return query(left, right, 2*idx)
            if mid+1 <= left and right <= j:
                return query(left, right, 2*idx+1)
            
            lval = query(left, mid, 2*idx)
            rval = query(mid+1, right, 2*idx+1)
            
            return lval+rval
        
        return query(left, right, 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)