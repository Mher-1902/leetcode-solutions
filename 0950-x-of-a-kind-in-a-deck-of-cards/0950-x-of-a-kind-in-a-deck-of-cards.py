from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        di = {}
        for i in deck:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        res = reduce(gcd,di.values())
        return res >= 2