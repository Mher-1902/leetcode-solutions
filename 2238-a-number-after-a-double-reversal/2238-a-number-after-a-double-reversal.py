class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        ls = [int(i) for i in str(num)]
        l = len(ls)-1
        while ls[l] == 0:
            if ls[l] == 0:
                ls.pop(l)
                l -= 1
        s = ''
        for i in ls:
            s += str(i)
        num1 = [num]
        num2 = [int(s)]
        if num2[::-1] == num1[::-1]:
            return True
        else:
            return False

        