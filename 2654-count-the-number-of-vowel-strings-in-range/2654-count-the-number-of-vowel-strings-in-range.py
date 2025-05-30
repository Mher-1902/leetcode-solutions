class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ls = ['a', 'e', 'i', 'o','u']
        cnt = 0
        for i in range(left,right+1):
            if words[i][0] in ls and words[i][-1] in ls:
                                cnt += 1
        return cnt
        