from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = 0
        freq = Counter(word)
        ls = []
        ans = float('inf')
        for a,b in freq.items():
            ls.append(b)
        for i in ls:
            x = i
            curr_del = 0
            for y in ls:
                if y < x:
                    curr_del += y
                elif y > x + k:
                    curr_del += (y - x -k)
            ans = min(ans,curr_del)
        return ans
                

        