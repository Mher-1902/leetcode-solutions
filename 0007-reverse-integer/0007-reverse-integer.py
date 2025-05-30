class Solution(object):
    def reverse(self, x):
        if not  -2**31 <= x <= 2**31 - 1:
                return 0
        st = str(x)
        if x < 0:
            st = st[1:]
        ls = []
        ls1 = []
        for i in st:
            ls.append(int(i))
        for j in ls[::-1]:
            ls1.append(j)
        st1 = ''
        for k in ls1:
            st1 = st1 + str(k)
        y = int(st1)
        if x < 0:
            y = -y
        if not  -2**31 <= y <= 2**31 - 1:
                return 0
        return y                
        