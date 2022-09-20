class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def is_palindrome(check):
            return check == check[::-1]
        
        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j != n and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        
        return valid_pals