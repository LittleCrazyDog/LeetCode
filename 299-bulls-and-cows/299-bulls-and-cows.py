class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        b = sum((s & g).values()) - a
        return "%sA%sB" % (a, b)