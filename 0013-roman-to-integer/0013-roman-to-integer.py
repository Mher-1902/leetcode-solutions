class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)-1):
            if di[s[i] ]< di[s[i+1]]:
                total -= di[s[i]]
            else:
                total += di[s[i]]
        total += di[s[-1]]
        return total
        