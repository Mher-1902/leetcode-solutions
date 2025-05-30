class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i1 = int(a,2)
        i2 = int(b,2)
        res = i1 + i2
        byd = bin(res)
        srt = str(byd)
        return srt[2:]
        