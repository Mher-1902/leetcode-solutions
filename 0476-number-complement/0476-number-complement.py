class Solution:
    def findComplement(self, num: int) -> int:
        res = bin(num)
        new_res = res[2:]
        new_res=new_res.replace('1','x')
        new_res=new_res.replace('0','1')
        new_res=new_res.replace('x','0')
        return int(new_res,2)