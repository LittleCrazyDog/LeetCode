class MagicDictionary:

    def __init__(self):
        self.wordsdict = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.wordsdict[len(word)] = self.wordsdict.get(len(word),[]) + [word]

    def search(self, searchWord: str) -> bool:
        for candi in self.wordsdict.get(len(searchWord), []):
            countdiff = 0
            for i in range(len(searchWord)):
                if candi[i] != searchWord[i]:
                    countdiff += 1
            if countdiff == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)