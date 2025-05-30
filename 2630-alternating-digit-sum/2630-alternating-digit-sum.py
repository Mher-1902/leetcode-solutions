class Solution:
    def alternateDigitSum(self, n: int) -> int:
        st = str(n)
        ls = []
        for i in st:
            ls.append(int(i))
        sl = ls
        for i in range(len(sl)):
            if i % 2 != 0:
                sl[i] = sl[i] * -1

        return sum(sl)