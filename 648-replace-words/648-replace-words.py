class Node:
    def __init__(self):
        self.sub = defaultdict(Node)
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        cur = self.root
        for ch in word: cur = cur.sub[ch]
        cur.word = word
    
    def find(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.sub: return word
            cur = cur.sub[ch]
            if cur.word is not None: return cur.word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = Trie()
        for word in dictionary: roots.insert(word)
        return ' '.join(roots.find(word) for word in sentence.split())