class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # DAG
        # 1. Initialize all letters in words with degree 0
        # 2. For each word i and word i+1 where i+1<n:
        #    If we find a letter a != letter b in word i and i+1:
        #    Add one to the degree and add letter b to letter a's set of letters, and go to the next word,
        #    since each word only tells us information about one pair of letters
        # 3. Go through all the degree==0s and add it to BFS queue
        # 4. While the bfs queue is not empty:
        #    Pop letter a and append it to the res string
        #    For each letter b in letter a's set of letters:
        #    subtract 1 from the degree, if it's degree is 0, add it to the queue
        #    Repeat 4
        # 5. If the size of the result string != the size of the initialized letters then return an empty
        #    string(not all of the degrees hit 0 so there is a conflict)
        # 6. Return the result string
        
        # map = {}
        # letters = [0 for _ in range(26)]
        # for i in range(len(words)):
        #     for j in range(len(words[i])):
        #         key = ord(words[i][j]) - ord('a')
        #         map[key] = set()
        # for i in range(len(words)-1):
        #     word1, word2 = words[i], words[i+1]
        #     for j in range(min(len(word1),len(word2))):
        #         if word1[j] != word2[j]:
        #             key1 = ord(word1[j]) - ord('a')
        #             key2 = ord(word2[j]) - ord('a')
        #             if key2 not in map[key1]:
        #                 letters[key2] += 1
        #                 map[key1].add(key2)
        #             break
        #         elif j == min(len(word1),len(word2)) - 1 and len(word1) > len(word2):
        #             return ''
        # q = deque()
        # res = ''
        # for i in range(26):
        #     if letters[i] == 0 and i in map:
        #         q.append(i)
        # while q:
        #     nextup = q.popleft()
        #     res += chr(nextup+ord('a'))
        #     for greater in map[nextup]:
        #         letters[greater] -= 1
        #         if letters[greater] == 0: q.append(greater)
        # return res if len(map) == len(res) else ''
        
        
        map = {}
        letters = [0 for _ in range(26)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                map[key] = set()
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    key1 = ord(word1[j]) - ord('a')
                    key2 = ord(word2[j]) - ord('a')
                    if key2 not in map[key1]:
                        letters[key2] += 1
                        map[key1].add(key2)
                    break
                elif j == min(len(word1),len(word2))-1 and len(word1) > len(word2):
                    return ''
        q = deque()
        res = ''
        for i in range(26):
            if letters[i] == 0 and i in map: q.append(i)
        while q:
            nextup = q.popleft()
            res += chr(nextup+ord('a'))
            for greater in map[nextup]:
                letters[greater] -= 1
                if letters[greater] == 0: q.append(greater)
        return res if len(map) == len(res) else ''
                