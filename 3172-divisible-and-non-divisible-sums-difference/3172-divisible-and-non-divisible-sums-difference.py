class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ls = []
        ls1 = []
        for i in range(1,n+1):
            if i % m != 0:
                ls.append(i)
        for i in range(1,n+1):
            if i % m == 0:
                ls1.append(i)
        return (sum(ls)-sum(ls1))
