class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect.bisect(list(accumulate(chalk)), k % sum(chalk))