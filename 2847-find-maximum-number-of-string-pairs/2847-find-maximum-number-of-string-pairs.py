class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        seen = set()
        for i in words:
            rev = i[::-1]
            if rev in seen:
                cnt += 1
            else:
                seen.add(i)
        return cnt
        