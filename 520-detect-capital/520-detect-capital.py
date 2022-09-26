class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        num_cap, n = 0, len(word)
        for letter in word:
            num_cap += letter.isupper()
        if num_cap == 0 or num_cap == n or num_cap == 1 and word[0].isupper():
            return True
        return False