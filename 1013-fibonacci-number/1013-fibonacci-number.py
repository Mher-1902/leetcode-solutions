class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0,1:1}
        def fib2(n):
            if n in memo:
                return memo[n]
            memo[n] = fib2(n-1) + fib2(n-2)
            return memo[n]
        return fib2(n)

        