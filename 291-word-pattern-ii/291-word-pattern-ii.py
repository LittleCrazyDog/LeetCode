class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.dfs(pattern, s, {})
    
    def dfs(self, pattern, s, dict):
        if len(pattern) == 0 and len(s) > 0:
            return False
        if len(pattern) == len(s) == 0:
            return True
        for end in range(1, len(s)-len(pattern)+2):
            if pattern[0] not in dict and s[:end] not in dict.values():
                dict[pattern[0]] = s[:end]
                if self.dfs(pattern[1:], s[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == s[:end]:
                if self.dfs(pattern[1:], s[end:], dict):
                    return True
        return False