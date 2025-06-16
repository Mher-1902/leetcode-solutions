from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        perc = 25/100 * len(arr)
        di = Counter(arr)
        for a,b in di.items():
            if b > perc:
                return a
        