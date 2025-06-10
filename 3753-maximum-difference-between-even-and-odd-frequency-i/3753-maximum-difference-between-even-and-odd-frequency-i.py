class Solution:
    def maxDifference(self, s: str) -> int:
        di  = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        odds = [i for i in di.values() if i % 2 == 1]
        evens = [i for i in di.values() if i % 2 == 0]
        if not odds or not evens:
            return 0
        return max(odd - even for odd in odds for even in evens)