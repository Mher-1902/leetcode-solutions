class Solution:
    def pivotInteger(self, n: int) -> int:
        ls=[i for i in range(1,n+1)]
        prefix_sum = [0] * (n+1)
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + ls[i-1]
        for i in range(1,n+1):
            l = prefix_sum[i]
            r = prefix_sum[n] - prefix_sum[i-1]
            if l == r:
                return i
        return -1