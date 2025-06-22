class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ls = [s[i:i+k] for i in range(0,len(s),k)]
        while len(ls[-1]) < k:
            ls[-1] += fill
        return ls