class MyHashMap:
    
    def eval_hash(self, key):
        return ((key*1031237) & ((1<<20)-1)) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))

    def get(self, key: int) -> int:
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key: return v
        return -1

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k, v))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)