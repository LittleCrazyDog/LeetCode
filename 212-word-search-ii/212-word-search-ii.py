class TrieNode():
    def __init__(self, char='', parent=None):
        self.char = char
        self.children = defaultdict()
        self.isWord = False
        self.num_of_words_downward = 0
        self.parent = parent
    
    def prune(self):
        while self.parent.parent:
            self.num_of_words_downward -= 1
            self = self.parent

class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                new_node = TrieNode(w)
                new_node.parent = node
                node.children[w] = new_node
            node = node.children[w]
            node.num_of_words_downward += 1
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        
        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res)
        
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
            node.prune()
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        tmp = board[i][j]
        if tmp not in node.children or node.children[tmp].num_of_words_downward == 0:
            return
        
        board[i][j] = '#'
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            self.dfs(board, node.children[tmp], i+dx, j+dy, path+tmp, res)
        board[i][j] = tmp
