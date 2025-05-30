class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ls = []
        res1 = []
        for i in range(left,right+1):
            ls.append(str(i))
        for i in ls:
            if len(i) == 1:
                res1.append(i)
        ls = [i for i in ls if i not in res1]
        res2 = []
        for i in ls:
            if '0' in i:
                continue
            res2.append(i)
        result = []
        for i in res2:
            num = int(i)
            if all(num % int(dig) == 0 for dig in i):
                result.append(num)
        res1 = [int(i) for i in res1]
        final_res = res1 + result
        return final_res
        