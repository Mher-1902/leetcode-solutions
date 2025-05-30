import functools
class Solution(object):
    @functools.cache
    def climbStairs(self, n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            else:
                two_back = self.climbStairs(n-2)
                one_back = self.climbStairs(n-1)
            return two_back + one_back
        