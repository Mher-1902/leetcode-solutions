import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ls = []
        for i in range(1,int(math.sqrt(num))+1):
            if num % i == 0:
                if i != num:
                    ls.append(i)
                if i != num // i and num // i != num:
                    ls.append(num//i)
        return sum(ls) == num 