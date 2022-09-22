class RandomizedCollection:

    def __init__(self):
        self.vals, self.idxs = [], defaultdict(set)

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.idxs[val].add(len(self.vals)-1)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()