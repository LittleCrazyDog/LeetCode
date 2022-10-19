class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([beginWord])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return depth
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            wordList.remove(next_word)
                            queue.append(next_word)
        return 0